from enum import IntEnum  
# ✅ Enum is used when you want to define a set of constant choices.
# Example: Todo status can only be 1 (Pending), 2 (In Progress), or 3 (Completed).
# Using IntEnum makes sure the values are integers but still readable as names.

from typing import List, Optional  
# ✅ List: Used when a field or response should hold multiple items (like a list of todos).
# ✅ Optional: Used when a field is not mandatory (can be None).
# Example: "todo_description" might be optional when creating a todo.

from pydantic import BaseModel, Field  
# ✅ BaseModel: All request/response models in FastAPI inherit from this.
# It validates input automatically (ensures correct types, required fields, etc.).
# ✅ Field: Lets you add extra rules or metadata for fields,
# like default values, min/max length, descriptions, or example data.
# Example: Field(..., min_length=3, max_length=50, description="Name of the todo")

from fastapi import FastAPI, HTTPException  
# ✅ FastAPI: The main FastAPI class.
# ✅ HTTPException: Used to raise custom HTTP exceptions.

api = FastAPI()
# ✅ api: The FastAPI instance.
# It is used to define routes and handle requests.


class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1
    
class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=50, description="Name of the todo")
    todo_description: str = Field(..., min_length=3, max_length=50, description="Description of the todo")
    priority: Priority = Field(default=Priority.LOW, description="Priority of the todo")
    
class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description="ID of the todo")

class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=50, description="Name of the todo")
    todo_description: Optional[str] = Field(None, min_length=3, max_length=50, description="Description of the todo")
    priority: Optional[Priority] = Field(None, description="Priority of the todo")
    
all_todos = [
    Todo(todo_id=1, todo_name="Sports", todo_description="Go to the gym", priority=Priority.LOW),
    Todo(todo_id=2, todo_name="Work", todo_description="Work on a project", priority=Priority.MEDIUM),
    Todo(todo_id=3, todo_name="Sleep", todo_description="Sleep well", priority=Priority.HIGH),
    Todo(todo_id=4, todo_name="Eat", todo_description="Eat well", priority=Priority.LOW),
    Todo(todo_id=5, todo_name="Meditate", todo_description="Meditate 20 minutes", priority=Priority.HIGH)
]


@api.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@api.get("/todos", response_model=List[Todo])
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    
    
@api.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1
    
    new_todo = Todo(
        todo_id = new_todo_id,
        todo_name = todo.todo_name,
        todo_description = todo.todo_description,
        priority = todo.priority
    )
    
    all_todos.append(new_todo)
    return new_todo


@api.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@api.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            delete_todo = all_todos.pop(index)
            return delete_todo
    raise HTTPException(status_code=404, detail="Todo not found")
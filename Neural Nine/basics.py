from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {'todo_id': 1, 'todo_name': 'sports', 'todo_description': 'go to the gym'},
    {'todo_id': 2, 'todo_name': 'work', 'todo_description': 'work on a project'},
    {'todo_id': 3, 'todo_name': 'sleep', 'todo_description': 'sleep well'},
    {'todo_id': 4, 'todo_name': 'eat', 'todo_description': 'eat well'},
    {'todo_id': 5, 'todo_name': 'meditate', 'todo_description': 'meditate 20 minutes'}
]

# SET, POST, PUT, DELETE

@api.get("/")
def index():
    return {"message": "Hello World"}


# localhost:9999/todos/2               Ist Path
# localhost:9999/todos?first_n=2       Ist Query

@api.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result': todo}

# int 2, str "2"
# (first_n = None) it take as string not int
@api.get("/todos")
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    
@api.post("/todos")
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1
    
    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }
    
    all_todos.append(new_todo)
    return new_todo

# Simple def without use of pydantic
@api.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = updated_todo['todo_name']
            todo['todo_description'] = updated_todo['todo_description']
            return todo
    return {'message': 'Todo not found'}

# Simple def without use of pydantic
@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            delete_todo = all_todos.pop(index)
            return delete_todo
    return {'message': 'Todo not found'}




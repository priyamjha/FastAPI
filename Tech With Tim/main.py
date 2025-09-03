from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks = []
# ✅ List to store tasks

@app.post("/tasks", response_model=Task) # ✅ Response model is used to specify the data type of the response
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_update: Task):
    #✅ Loop through the list of tasks and also keep track of the index
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            # ✅ Creates a copy of the existing task and updates only the fields 
            # provided in task_update (exclude_unset=True ignores fields that were not sent)
            tasks[index] = updated_task
            # ✅ Replace the old task in the list with the updated task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")




if __name__ == "__main__":  
    # ✅ This ensures the code below runs only when 
    # this file is executed directly (python main.py),
    # not when it's imported as a module in another file.
    
    import uvicorn
    # ✅ Uvicorn is an ASGI server used to run FastAPI apps.
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # ✅ Starts the FastAPI app on http://localhost:8000
    # host="0.0.0.0" → accessible from any device on the network
    # port=8000 → the port number where API will run

from fastapi import FastAPI
from pydantic import BaseModel # Use for data validation
from typing import List


app = FastAPI() # Create a FastAPI instance


class Tea(BaseModel):   # Create a Pydantic model
    id: int
    name: str
    origin: str
    
teas: List[Tea] = []    # List to store teas


@app.get("/")  # Decorator
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/teas")
def read_teas():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return {"message": "Tea added successfully"}

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    # for t in teas:
    #     if t.id == tea_id:
    #         t.name = updated_tea.name
    #         t.origin = updated_tea.origin
    #         return {"message": "Tea updated successfully"}
    # return {"message": "Tea not found"}
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return {"message": "Tea updated successfully"}
    return {"error": "Tea not found"}

@app.delete('/teas/{tea_id}')
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas.pop(index)
            return {"message": "Tea deleted successfully"}
    return {"error": "Tea not found"}
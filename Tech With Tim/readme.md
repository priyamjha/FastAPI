````markdown
## 🚀 How to Run the App

Unlike the usual `uvicorn main:app` command, this project is set up to run directly with Python.

1. Make sure you have **FastAPI** and **Uvicorn** installed:

```bash
pip install fastapi uvicorn
````

2. Start the server by running:

```bash
python main.py
```

This works because in `main.py` we added:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

So, the app starts automatically with `python main.py`.

---

## 🌐 API Documentation

Once the server is running, you can access:

* **Swagger UI (interactive docs):**
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* **ReDoc (alternative docs):**
  👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📝 Notes

### 🔁 Using `enumerate()`

`enumerate(tasks)` lets you loop through both the **index** and the **task object**.
You need the index because if you want to update or replace a task inside the list, you must know its position.

---

### ⚡ FastAPI + Pydantic v2 Changes

FastAPI recently upgraded to **Pydantic v2**.

The method `.dict()` in class `BaseModel` is deprecated.
Instead, use `.model_dump()`.

Example update code:

```python
# ❌ Old (Pydantic v1)
updated_task = task.copy(update=task_update.dict(exclude_unset=True))

# ✅ New (Pydantic v2)
updated_task = task.copy(update=task_update.model_dump(exclude_unset=True))
```

### 🔑 Key changes in Pydantic v2:

* `.dict()` → `.model_dump()`
* `.json()` → `.model_dump_json()`

```

````markdown
# 🚀 FastAPI Project

This project is built with **FastAPI** and can be run in multiple ways depending on your needs.  
Follow the instructions below to get started.

---

## ⚡ How to Run FastAPI

There are two common ways to start your FastAPI app using **Uvicorn**:

1. **Normal Run**
```bash
uvicorn main:app
````

This runs the app normally.

2. **With Reload**

```bash
uvicorn main:app --reload
```

The `--reload` flag automatically restarts the server whenever you make changes to the code.
This is very useful during development.

---

## 🔧 Run FastAPI on a Custom Port

You can start your FastAPI app on a different port instead of the default `8000`.

### Using Uvicorn

```bash
uvicorn main:api --port 9999
```

Here:

* `main` → your Python file name (`main.py`)
* `api` → the FastAPI instance (`api = FastAPI()`)
* `--port 9999` → runs the server on port **9999**

---

### Using FastAPI CLI (Pydantic v2 / FastAPI v0.100+)

```bash
fastapi dev main.py --port 9999
```

This also runs the app on **port 9999**, with auto-reload enabled by default.

---

## 🐍 Run the App with Python (Custom Setup)

Unlike the usual `uvicorn main:app` command, this project is also set up to run directly with **Python**.

1. Install dependencies:

```bash
pip install fastapi uvicorn
```

2. Start the server:

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

The method `.dict()` in class `BaseModel` is **deprecated**.
Instead, use `.model_dump()`.

#### Example update code:

```python
# ❌ Old (Pydantic v1)
updated_task = task.copy(update=task_update.dict(exclude_unset=True))

# ✅ New (Pydantic v2)
updated_task = task.copy(update=task_update.model_dump(exclude_unset=True))
```

#### 🔑 Key changes in Pydantic v2:

* `.dict()` → `.model_dump()`
* `.json()` → `.model_dump_json()`

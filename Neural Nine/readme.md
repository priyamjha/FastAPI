````markdown
## 🚀 Run FastAPI on a Custom Port

You can start your FastAPI app on a different port instead of the default `8000`.

### Using Uvicorn
```bash
uvicorn main:api --port 9999
````

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

```
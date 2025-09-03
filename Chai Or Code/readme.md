````markdown
## 🚀 How to Run FastAPI

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

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import engine, get_db

# Instructs SQLAlchemy to automatically construct missing SQL tables on boot
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Advanced Task Manager")
templates = Jinja2Templates(directory="templates")

# Serves the user interface layout

# Serves the user interface layout
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    # Fix: Explicitly name the context keyword argument
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"request": request}
    )



# --- CRUD API ENDPOINTS ---


@app.post("/api/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        completed=task.completed
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get("/api/tasks", response_model=List[schemas.TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


@app.put("/api/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task_status(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.completed = not db_task.completed
    db.commit()
    db.refresh(db_task)
    return db_task


@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}

from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=List[schemas.Task])
def list_tasks(
    skip: int = 0,
    limit: int = 100,
    status_filter: Optional[models.TaskStatus] = Query(None, alias="status"),
    employee_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    return crud.get_tasks(
        db,
        skip=skip,
        limit=limit,
        status=status_filter,
        employee_id=employee_id,
    )


@router.get("/{task_id}", response_model=schemas.Task)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.post(
    "/",
    response_model=schemas.Task,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
):
    emp = crud.get_employee(db, task.employee_id)
    if not emp:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Employee does not exist")

    return crud.create_task(db, task)


@router.put("/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: int,
    updates: schemas.TaskUpdate,
    db: Session = Depends(get_db),
):
    db_task = crud.get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    if updates.employee_id is not None:
        emp = crud.get_employee(db, updates.employee_id)
        if not emp:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Employee does not exist")

    return crud.update_task(db, db_task, updates)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    db_task = crud.get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    crud.delete_task(db, db_task)
    return None

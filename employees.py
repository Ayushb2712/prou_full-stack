from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/", response_model=List[schemas.Employee])
def list_employees(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return crud.get_employees(db, skip=skip, limit=limit)


@router.get("/{employee_id}", response_model=schemas.Employee)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
):
    emp = crud.get_employee(db, employee_id)
    if not emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return emp


@router.post(
    "/",
    response_model=schemas.Employee,
    status_code=status.HTTP_201_CREATED,
)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db),
):
    existing = crud.get_employee_by_email(db, employee.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    return crud.create_employee(db, employee)


@router.put("/{employee_id}", response_model=schemas.Employee)
def update_employee(
    employee_id: int,
    updates: schemas.EmployeeUpdate,
    db: Session = Depends(get_db),
):
    db_emp = crud.get_employee(db, employee_id)
    if not db_emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

    return crud.update_employee(db, db_emp, updates)


@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
):
    db_emp = crud.get_employee(db, employee_id)
    if not db_emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

    crud.delete_employee(db, db_emp)
    return None


@router.get("/{employee_id}/tasks", response_model=List[schemas.Task])
def list_employee_tasks(
    employee_id: int,
    db: Session = Depends(get_db),
):
    emp = crud.get_employee(db, employee_id)
    if not emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

    return emp.tasks

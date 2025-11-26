from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas


def get_employee(db: Session, employee_id: int) -> Optional[models.Employee]:
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employee_by_email(db: Session, email: str) -> Optional[models.Employee]:
    return db.query(models.Employee).filter(models.Employee.email == email).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100) -> List[models.Employee]:
    return db.query(models.Employee).offset(skip).limit(limit).all()


def create_employee(db: Session, employee: schemas.EmployeeCreate) -> models.Employee:
    db_emp = models.Employee(**employee.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp


def update_employee(
    db: Session,
    db_employee: models.Employee,
    updates: schemas.EmployeeUpdate,
) -> models.Employee:
    data = updates.dict(exclude_unset=True)
    for field, value in data.items():
        setattr(db_employee, field, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, db_employee: models.Employee) -> None:
    db.delete(db_employee)
    db.commit()


def get_task(db: Session, task_id: int) -> Optional[models.Task]:
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    status: Optional[models.TaskStatus] = None,
    employee_id: Optional[int] = None,
) -> List[models.Task]:
    query = db.query(models.Task)
    if status is not None:
        query = query.filter(models.Task.status == status)
    if employee_id is not None:
        query = query.filter(models.Task.employee_id == employee_id)
    return query.offset(skip).limit(limit).all()


def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(
    db: Session,
    db_task: models.Task,
    updates: schemas.TaskUpdate,
) -> models.Task:
    data = updates.dict(exclude_unset=True)
    for field, value in data.items():
        setattr(db_task, field, value)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, db_task: models.Task) -> None:
    db.delete(db_task)
    db.commit()

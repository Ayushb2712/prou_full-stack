from datetime import date
from typing import List, Optional

from pydantic import BaseModel, EmailStr

from .models import EmployeeStatus, TaskStatus


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo
    due_date: Optional[date] = None
    employee_id: int


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    due_date: Optional[date] = None
    employee_id: Optional[int] = None


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    role: str
    status: EmployeeStatus = EmployeeStatus.active


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    status: Optional[EmployeeStatus] = None


class Employee(EmployeeBase):
    id: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True

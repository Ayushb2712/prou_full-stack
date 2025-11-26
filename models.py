import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Text, Date
from sqlalchemy.orm import relationship

from .database import Base


class EmployeeStatus(str, enum.Enum):
    active = "ACTIVE"
    inactive = "INACTIVE"


class TaskStatus(str, enum.Enum):
    todo = "TODO"
    in_progress = "IN_PROGRESS"
    done = "DONE"


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    role = Column(String(100), nullable=False)
    status = Column(Enum(EmployeeStatus), nullable=False, default=EmployeeStatus.active)

    tasks = relationship(
        "Task",
        back_populates="employee",
        cascade="all, delete-orphan",
    )


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.todo)
    due_date = Column(Date, nullable=True)

    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    employee = relationship("Employee", back_populates="tasks")

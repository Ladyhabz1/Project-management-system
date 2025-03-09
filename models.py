from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Table
from sqlalchemy.orm import relationship
from database import Base
import datetime

# Many-to-Many Relationship Table
employee_task = Table(
    "employee_task",
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("employees.id"), primary_key=True),
    Column("task_id", Integer, ForeignKey("tasks.id"), primary_key=True)
)

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    deadline = Column(DateTime)

    tasks = relationship("Task", back_populates="project")    

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String)

    tasks = relationship("Task", secondary=employee_task, back_populates="employees")     

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    deadline = Column(DateTime)
    priority = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="tasks")
    employees = relationship("Employee", secondary=employee_task, back_populates="tasks")

    

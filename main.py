import click
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Project, Employee, Task, task_employee_association
import datetime

@click.group()
def cli():
    """Project Management System CLI"""
    pass

@click.command()
@click.argument("name")
@click.argument("description")
@click.argument("deadline")
def add_project(name, description, deadline):
    """Add a new project"""
    session = SessionLocal()
    project = Project(name=name, description=description, deadline=datetime.datetime.strptime(deadline, "%Y-%m-%d"))
    session.add(project)
    session.commit()
    session.close()
    click.echo(f"Project '{name}' added successfully!")

@click.command()
@click.argument("name")
@click.argument("role")
def add_employee(name, role):
    """Add a new employee"""
    session = SessionLocal()
    employee = Employee(name=name, role=role)
    session.add(employee)
    session.commit()
    session.close()
    click.echo(f"Employee '{name}' added successfully!")

@click.command()
@click.argument("title")
@click.argument("description")
@click.argument("deadline")
@click.argument("priority")
@click.argument("project_id", type=int)
def add_task(title, description, deadline, priority, project_id):
    """Add a new task"""
    session = SessionLocal()
    task = Task(
        title=title, 
        description=description, 
        deadline=datetime.datetime.strptime(deadline, "%Y-%m-%d"), 
        priority=priority, 
        project_id=project_id,
        completed=False
    )
    session.add(task)
    session.commit()
    session.close()
    click.echo(f"Task '{title}' added successfully!")

@click.command()
@click.argument("task_id", type=int)
@click.argument("employee_id", type=int)
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

def assign_employee(task_id, employee_id):
    """Assign an employee to a task"""
    session = SessionLocal()
    task = session.query(Task).filter_by(id=task_id).first()
    employee = session.query(Employee).filter_by(id=employee_id).first()
    if task and employee:
        task.employees.append(employee)
        session.commit()
        click.echo(f"Employee '{employee.name}' assigned to task '{task.title}'")
    else:
        click.echo("Invalid task or employee ID.")
    session.close()

@click.command()

def list_projects():
    """List all projects with progress"""
    session = SessionLocal()
    projects = session.query(Project).all()
    for project in projects:
        total_tasks = session.query(Task).filter_by(project_id=project.id).count()
        completed_tasks = session.query(Task).filter_by(project_id=project.id, completed=True).count()
        progress = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        click.echo(f"{project.id}: {project.name} (Deadline: {project.deadline}, Progress: {progress:.2f}%)")
    session.close()

@click.command()

def list_pending_tasks():
    """List all pending tasks"""
    session = SessionLocal()
    tasks = session.query(Task).filter_by(completed=False).all()
    for task in tasks:
        click.echo(f"{task.id}: {task.title} (Deadline: {task.deadline}, Priority: {task.priority})")
    session.close()

@click.command()
@click.argument("employee_id", type=int)

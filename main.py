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
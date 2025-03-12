import click
from sqlalchemy.orm import sessionmaker
from database import engine, sessionLocal
from models import Project, Task, Employee
from datetime import datetime

# Create session factory
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

@click.group()
def cli():
    """Project Management CLI"""
    pass

@click.command()
@click.argument('name')
@click.option('--description', default="", help='Project description')
@click.option('--deadline', type=str, help='Project deadline (YYYY-MM-DD)')
def create_project(name, description, deadline):
    """Create a new project"""
    session = get_session()
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d") if deadline else None
        project = Project(name=name, description=description, deadline=deadline_date)
        session.add(project)
        session.commit()
        click.echo(f"Project '{name}' created successfully!")
    except Exception as e:
        click.echo(f"Error creating project: {e}")
    finally:
        session.close()

@click.command()
@click.argument('project_id', type=int)
@click.argument('title')
@click.argument('description')
@click.option('--deadline', type=str, help='Task deadline (YYYY-MM-DD)')
@click.option('--priority', type=click.Choice(['Low', 'Medium', 'High']), default='Medium', help='Task priority')
def add_task(project_id, title, description, deadline, priority):
    """Add a new task to a project"""
    session = get_session()
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d") if deadline else None
        task = Task(project_id=project_id, title=title, description=description, deadline=deadline_date, priority=priority)
        session.add(task)
        session.commit()
        click.echo(f"Task '{title}' added to project {project_id}.")
    except Exception as e:
        click.echo(f"Error adding task: {e}")
    finally:
        session.close()

@click.command()
@click.argument('task_id', type=int)
@click.argument('employee_id', type=int)
def assign_employee(task_id, employee_id):
    """Assign an employee to a task"""
    session = get_session()
    try:
        task = session.get(Task, task_id)
        employee = session.get(Employee, employee_id)
        if task and employee:
            task.employees.append(employee)
            session.commit()
            click.echo(f"Employee {employee.name} assigned to task {task.name}.")
        else:
            click.echo("Task or Employee not found.")
    except Exception as e:
        click.echo(f"Error assigning employee: {e}")
    finally:
        session.close()

@click.command()
def view_workload():
    """View employee workload"""
    session = get_session()
    try:
        employees = session.query(Employee).all()
        for emp in employees:
            tasks_count = len(emp.tasks)
            click.echo(f"Employee {emp.name} (ID: {emp.id}) has {tasks_count} tasks.")
    except Exception as e:
        click.echo(f"Error viewing workload: {e}")
    finally:
        session.close()

@click.command()
def generate_report():
    """Generate report on task completion and employee performance"""
    session = get_session()
    try:
        tasks = session.query(Task).all()
        completed_tasks = [task for task in tasks if task.completed]
        click.echo(f"Total Tasks: {len(tasks)}, Completed Tasks: {len(completed_tasks)}")
        
        employees = session.query(Employee).all()
        for emp in employees:
            assigned_tasks = len(emp.tasks)
            completed = sum(1 for task in emp.tasks if task.completed)
            click.echo(f"Employee {emp.name}: {completed}/{assigned_tasks} tasks completed.")
    except Exception as e:
        click.echo(f"Error generating report: {e}")
    finally:
        session.close()

# Add commands to CLI
cli.add_command(create_project)
cli.add_command(add_task)
cli.add_command(assign_employee)
cli.add_command(view_workload)
cli.add_command(generate_report)

if __name__ == '__main__':
    cli()

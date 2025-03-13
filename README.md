# Project Management System (CLI)

The **Project Management System** is a command-line interface (CLI) application designed to efficiently manage projects, employees, and tasks. It enables tracking assignments, deadlines, and progress to ensure smooth project execution.

Built using **Python, Click, and SQLAlchemy ORM**, this project ensures persistent data storage and an interactive CLI experience.

## Table of Contents
- [Features](#features)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Testing](#testing)
- [Contribution](#contributing)
- [License](#license)

## Features
1. **Project Management** – Create and manage projects with associated tasks.
2. **Task Management** – Assign multiple employees to a task.
3. **Task Prioritization & Deadlines** – Set priority levels (High, Medium, Low) and deadlines for tasks.
4. **Employee Workload Analysis** – View employee workload.
5. **Report Generation** – Generate reports on task completion and employee performance.
6. **Interactive CLI** – User-friendly navigation powered by Click.

## Installation and Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/Ladyhabz1/Project_management_system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd project_management_system
    ```
3. Create a Virtual Environment:
    ```bash
    python -m venv env
    ```
4. Activate the Virtual Environment:
    - On Windows (Command Prompt):
      ```bash
      env\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source env/bin/activate
      ```
5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Setup the database:
    ```bash
    python -m alembic upgrade head    ```

## Usage
To run the CLI, use:
 ```bash
 python main.py
 ```
 ## Testing

 After installing dependencies and setting up the database, follow these steps to manually verify that everything is working correctly.
---

### 1. Verify the Database Setup

Check if the database was created successfully:

```bash
sqlite3 database.db .tables
```
-If this command lists tables like projects, tasks, and employees, the database setup is correct.

### 2. Run The Cli
```bash
 python main.py
 ```
 You should see a list of available commands

 ### 3. Test Creating a Project
 ```bash
python main.py create-project "AI Research" --description "AI Trend Analysis" --deadline "2025-12-31"
```
#### **Project Commands**

| Command         | Description                      |
|-----------------|----------------------------------|
| `create-project`| Add a new project                |

 ### 4. Adding Task to project
 ```bash
python main.py add-task 1 "Data Collection" "Gather data for AI model" --deadline "2025-10-10" --priority High
```
### 5. Assigning Employee to a task
 ```bash
python main.py assign-employee 1 1
```
#### **Task Commands**

| Command            | Description                      |
|--------------------|----------------------------------|
| `add-task`         | Add a new task                   |
| `assign-employee`  | Assign an employee to a task     |

 ### 6. Adding an Employee
 ```bash
python main.py add-employee "John Doe" "Developer"
```
### 7. viewing the workload
 ```bash
python main.py view-workload
```
#### **Employee Commands**

| Command          | Description                              |
|-----------------|----------------------------------------|
| `add-employee`  | Add a new employee                      |
| `view-workload` | Show the workload distribution of employees |

### 8. Generate report on task completion
```bash
python main.py view-workload
```
#### **Report Commands**

| Command           | Description                                      |
|------------------|--------------------------------------------------|
| `generate-report` | Generate reports on task completion & performance |

### Contribution
Want to contribute? Follow these steps:
1. Fork the repository
2. Create a new branch 
    ```bash
    git checkout -b Your-Feature-Name
    ```
3. Make your changes
4. Commit changes 
    ```bash
    git commit -m 'Added new feature'
    ```
5. Push to GitHub 
    ```bash
    git push origin Your-Feature-Name
    ```
6. Submit a Pull Request

### License
This project is open-source and available under the MIT License.

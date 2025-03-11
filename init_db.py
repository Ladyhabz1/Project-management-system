from database import engine, Base
from models import Project, Employee, Task  # Ensure all models are imported

Base.metadata.create_all(engine)
print("Database tables created successfully!")

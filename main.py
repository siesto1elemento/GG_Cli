
import typer
import json
from pathlib import Path

app = typer.Typer()
tasks_file = Path("tasks.json")

if tasks_file.exists():
    with open(tasks_file, "r") as file:
        tasks = json.load(file)
else:
    tasks = {}


@app.command()
def add_task():
    task_description = typer.prompt("Enter the task")
    complete_by = typer.prompt("How much time to allot for this task in days")
    
    tasks[task_description] = complete_by
    
    with open(tasks_file, "w") as file:
        json.dump(tasks, file)
    
    print(tasks)


if __name__ == "__main__":
    app()


# project_management.py
import datetime
from project import Project

FILENAME = "projects.txt"

def load_projects(filename=FILENAME):
    """Load projects from a text file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
            projects.append(project)
    return projects

def save_projects(projects, filename=FILENAME):
    """Save projects to a text file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    print("Incomplete projects:")
    incomplete_projects = sorted([p for p in projects if not p.is_complete()])
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    completed_projects = sorted([p for p in projects if p.is_complete()])
    for project in completed_projects:
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Display projects starting after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = sorted([p for p in projects if p.starts_after(filter_date)], key=lambda p: p.start_date)
    for project in filtered_projects:
        print(f"  {project}")

def add_new_project(projects):
    """Add a new project based on user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)

def update_project(projects):
    """Update an existing project's completion and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(project)
    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)

def main():
    """Main program to manage projects."""
    projects = load_projects()
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {FILENAME}")

    MENU = """\n- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Enter filename to save projects to: ")
            save_projects(projects, filename)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    if input("Would you like to save to projects.txt? (y/n): ").lower() == "y":
        save_projects(projects)
        print("Projects saved to projects.txt")
    print("Thank you for using custom-built project management software.")

if __name__ == "__main__":
    main()

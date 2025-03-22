import os


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def is_completed(self):
        return self.completion_percentage == 100

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"


def load_projects(filename="projects.txt"):
    """Load projects from a given filename into a list of Project objects."""
    projects = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            file.readline()  # Skip the header line
            for line in file:
                parts = line.strip().split('\t')  # Split the line into parts by tab
                if len(parts) == 5:  # Ensure there are 5 columns
                    name, start_date, priority, cost_estimate, completion_percentage = parts
                    project = Project(
                        name,
                        start_date,
                        int(priority),
                        float(cost_estimate),
                        int(completion_percentage)
                    )
                    projects.append(project)
    return projects


def save_projects(projects, filename="projects.txt"):
    """Save projects to a given filename."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects."""
    print("Incomplete projects: ")
    for project in projects:
        if not project.is_completed():
            print(f"  {project}")

    print("Completed projects: ")
    for project in projects:
        if project.is_completed():
            print(f"  {project}")


def update_project(projects):
    """Update the completion percentage and priority of a project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        project_choice = int(input("Project choice: "))
        if project_choice < 0 or project_choice >= len(projects):
            print("Invalid choice.")
            return

        project = projects[project_choice]
        print(f"{project}")

        new_percentage = int(input("New Percentage: "))
        project.completion_percentage = new_percentage
        new_priority = int(input("New Priority: "))
        project.priority = new_priority
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    try:
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion_percentage = int(input("Percent complete: "))

        new_project = Project(
            name,
            start_date,
            priority,
            cost_estimate,
            completion_percentage
        )
        projects.append(new_project)
    except ValueError:
        print("Invalid input. Please enter valid values.")


def filter_projects_by_date(projects):
    """Filter projects by a starting date."""
    filter_date = input("Show projects that start after date (dd/mm/yy): ")
    for project in projects:
        if project.start_date > filter_date:
            print(f"{project}")


def main():
    projects = load_projects("projects.txt")
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            projects = load_projects("projects.txt")
            print(f"Loaded {len(projects)} projects from projects.txt")

        elif choice == 's':
            save_projects(projects)
            print("Projects saved.")

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            filter_projects_by_date(projects)

        elif choice == 'a':
            add_project(projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? (y/n): ").lower()
            if save_choice == 'y':
                save_projects(projects)
            print("Thank you for using custom-built project management software.")
            break


if __name__ == "__main__":
    main()

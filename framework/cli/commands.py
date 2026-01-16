import typer

app = typer.Typer(
        help="Burmese-Py a backend framework with a powerfull cli"
        )

@app.command()
def run():
    """
    Runs the project.
    """
    url = "http://localhost:8000"
    print(f"Running on port 8000: \033[94;4m{url}\033[0m")

new_app = typer.Typer(
        help="Create new resources (e.g., projects)."
        )

@new_app.command()
def project(name: str):
    """
    Creates a new project with the given name.
    """
    print(f"Creating project: {name}")

app.add_typer(new_app, name="new")

generate_app = typer.Typer(
        help="Generates new files (e.g., contollers, services, models)."
        )

@generate_app.command()
def controller(name: str):
    """
    Generates new controller file on a controllers folder.
    """
    print(f"Generating \033[92mcontrollers/{name}.py\033[0m ...")

@generate_app.command()
def service(name: str):
    """
    Generates new service file on a services folder.
    """
    print(f"Generating \033[92mservices/{name}.py\033[0m ...")

@generate_app.command()
def model(name: str):
    """
    Generates new model file on a models folder.
    """
    print(f"Generating \033[92mmodels/{name}.py\033[0m ...")

app.add_typer(generate_app, name="generate")

if __name__ == "__main__":
    app()
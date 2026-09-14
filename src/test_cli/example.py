import typer
from typing import Annotated
from rich import print

app = typer.Typer()

@app.command("printex")
def cli_print_dict() -> None:
    """Print a fancy dictionary."""
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    print(my_dict)

@app.command("leave")
def cli_leave(name: Annotated[str, typer.Argument(help="Name of the person to leave.")] = "Anonymous") -> None:
    """Print a goodbye message."""
    while True:
        print(f"Goodbye, {name}!")
        if (len(name) > 6):
            raise typer.Exit()
        else:
            raise typer.Abort()
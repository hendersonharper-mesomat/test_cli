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

@app.command("four-tuple")
def cli_four_tuple(tup: Annotated[tuple[int, int, int, int], typer.Argument(help="A tuple of four integers.")] = (1,2,3,4)) -> None:
    """Print the four-tuple."""
    print(f"The four-tuple is: {tup}")

@app.command("list")
def cli_list(items: Annotated[list[str], typer.Argument(help="A list of strings.")] = ["item1", "item2", "item3"]) -> None:
    """Print the list."""
    print(f"The list is: {items}")

@app.command("range-prompt")
def cli_range_prompt(
    start: Annotated[
        int, typer.Option(
            prompt=True,
            help="The starting value of the range."
        )] = 0, 
    end: Annotated[
        int, typer.Option(
            prompt=True,
            help="The ending value of the range."
        )] = 10) -> None:
    """Print a range of numbers."""
    print(f"The range is: {list(range(start, end))}")
import typer

from . import example, lookup

app = typer.Typer()
app.add_typer(example.app, name="example")
app.add_typer(lookup.app, name="lookup")


def main() -> None:
    app()

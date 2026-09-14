import typer
import webbrowser

app = typer.Typer()

@app.command("google")
def cli_google(search_string: str) -> None:
    """Open a tab in the default web browser that searches the source for the given string."""
    url = f"https://www.google.com/search?q={search_string}"
    webbrowser.open(url)

@app.command("youtube")
def cli_youtube(search_string: str, v: bool = False) -> None:
    """Open a tab in the default web browser that searches YouTube for the given string."""
    if v:
        url = f"https://www.youtube.com/watch?v={search_string}"
    else:
        url = f"https://www.youtube.com/results?search_query={search_string}"
    webbrowser.open(url)

@app.command("rickroll")
def cli_rickroll() -> None: #so you see you can do different names
    """Open a tab in the default web browser that rickrolls the user."""
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(url)
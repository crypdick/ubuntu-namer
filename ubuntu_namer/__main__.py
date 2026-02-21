import random
import string

import typer
from rich.console import Console

from .names import ubuntu_names

app = typer.Typer(
    name="ubuntu-namer",
    help="Generate random Ubuntu-style names.",
    add_completion=False,
)
console = Console()


@app.command(name="")
def generate_name(letter: str | None = None) -> str:
    """Generate a random Ubuntu-style name like 'Agile Amoeba'."""
    if letter is None:
        letter = random.choice(string.ascii_lowercase)
    elif isinstance(letter, str):
        if len(letter) != 1:
            raise ValueError(f"letter must be a single letter, got {len(letter)}")
        assert (
            letter in string.ascii_letters
        ), f"letter must be an alphabetical character, got {letter}"
        letter = letter.lower()
    else:
        raise ValueError(f"letter must be a str dtype, got {type(letter)}")

    adjective = random.choice(ubuntu_names[letter]["adjectives"])
    animal = random.choice(ubuntu_names[letter]["animals"])

    ubuntu_name = f"{adjective} {animal}".strip().title()

    console.print(f"[bold red]{ubuntu_name}[/]")

    return ubuntu_name


if __name__ == "__main__":
    app()

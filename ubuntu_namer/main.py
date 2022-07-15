# type: ignore[attr-defined]
from typing import Optional

import random
import string

import typer
from __init__ import version
from names import ubuntu_names
from rich.console import Console

app = typer.Typer(
    name="ubuntu-namer",
    help="Awesome `ubuntu-namer` is a Python port of ubuntu-name-generator",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]ubuntu-namer[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="")
def generate_name(
    letter: Optional[str] = None,
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the ubuntu-namer package.",
    ),
) -> str:
    """
    Generates a random Ubuntu name

    Args:
        letter: a letter to use for the first letter of the name. If none is given, a random letter is used.

    Returns:
        A random Ubuntu name

    Examples:
        .. code:: python

            >>> generate_name("V")
            "Veracious Viper"
    """
    type(print_version)  # this is just to make linter happy
    if letter is None:
        letter = random.choice(string.ascii_lowercase)
    elif isinstance(letter, str):
        assert len(letter) == 1, f"letter must be a single character, got {letter}"
        letter = letter.lower()
        assert (
            letter in string.ascii_lowercase
        ), f"letter must be a lowercase character, got {letter}"
    else:
        raise ValueError(f"letter must be a single character, got {letter}")

    adjective = random.choice(ubuntu_names[letter]["adjectives"])
    animals = random.choice(ubuntu_names[letter]["animals"])

    ubuntu_name = f"{adjective} {animals}"

    console.print(f"[bold red]{ubuntu_name}[/]")

    return ubuntu_name


# def main(
#     letter: str = typer.Option(..., help="The first letter of the name"),
# ) -> None:
#     """Print a greeting with a giving name."""
#     ubuntu_name = generate_name(letter)
#
#     console.print(ubuntu_name)


if __name__ == "__main__":
    app()

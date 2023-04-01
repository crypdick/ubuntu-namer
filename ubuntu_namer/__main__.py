# type: ignore[attr-defined]
from typing import Optional

import random
import string

import typer
from rich.console import Console

# from __init__ import version
from .names import ubuntu_names

app = typer.Typer(
    name="ubuntu-namer",
    help="Awesome `ubuntu-namer` is a Python port of ubuntu-name-generator",
    add_completion=False,
)
console = Console()


# def version_callback(print_version: bool) -> None:
#     """Print the version of the package."""
#     if print_version:
#         console.print(f"[yellow]ubuntu-namer[/] version: [bold blue]{version}[/]")
#         raise typer.Exit()


@app.command(name="")
def generate_name(
    letter: Optional[str] = None,
    # print_version: bool = typer.Option(
    #     None,
    #     "-v",
    #     "--version",
    #     callback=version_callback,
    #     is_eager=True,
    #     help="Prints the version of the ubuntu-namer package.",
    # ),
) -> str:
    """
    Generates a random Ubuntu name

    Args:
        letter: a letter to use for the first letter of the name. If none is given, a random letter is used.

    Returns:
        A random Ubuntu name

    Raises:
        ValueError: if the letter is not a single letter
        AssertionError: if the letter is not in the alphabet, e.g. "1"
        ValueError: if the letter is not a str dtype

    Examples:
        .. code:: python

            >>> generate_name("V")
            "Veracious Viper"
    """
    if letter is None:
        letter = random.choice(string.ascii_lowercase)
    elif isinstance(letter, str):
        if len(letter) != 1:
            raise ValueError(f"letter must be a single letter, got {len(letter)}")
        assert (
            letter in string.ascii_letters
        ), f"letter must be a alphabetical character, got {letter}"
        letter = letter.lower()
    else:
        raise ValueError(f"letter must be a str dtype, got {type(letter)}")

    adjective = random.choice(ubuntu_names[letter]["adjectives"])
    animals = random.choice(ubuntu_names[letter]["animals"])

    ubuntu_name = f"{adjective} {animals}".strip().title()

    console.print(f"[bold red]{ubuntu_name}[/]")

    return ubuntu_name


if __name__ == "__main__":
    app()

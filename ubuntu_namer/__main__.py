import random
import string
from typing import Literal

import typer
from rich.console import Console

from .names import ubuntu_names

NameStyle = Literal[
    "title", "lower", "upper", "camel", "pascal", "snake", "kebab", "dot"
]

STYLES: list[str] = list(NameStyle.__args__)

app = typer.Typer(
    name="ubuntu-namer",
    help="Generate random Ubuntu-style names.",
    add_completion=False,
)
console = Console()


def _format_name(adjective: str, animal: str, style: NameStyle) -> str:
    """Format an adjective-animal pair according to the given style."""
    adj = adjective.lower()
    ani = animal.lower()

    match style:
        case "title":
            return f"{adj.title()} {ani.title()}"
        case "lower":
            return f"{adj} {ani}"
        case "upper":
            return f"{adj.upper()} {ani.upper()}"
        case "camel":
            return f"{adj}{ani.title()}"
        case "pascal":
            return f"{adj.title()}{ani.title()}"
        case "snake":
            return f"{adj}_{ani}"
        case "kebab":
            return f"{adj}-{ani}"
        case "dot":
            return f"{adj}.{ani}"
        case _:
            raise ValueError(
                f"Unknown style {style!r}. Must be one of: {', '.join(STYLES)}"
            )


def generate_name(
    letter: str | None = None, *, style: NameStyle = "title"
) -> str:
    """Generate a random Ubuntu-style name like 'Agile Amoeba'.

    Args:
        letter: Starting letter (a-z). Random if None.
        style: Formatting style. One of: title, lower, upper, camel,
               pascal, snake, kebab, dot.

    Returns:
        A formatted name string.
    """
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

    return _format_name(adjective, animal, style)


@app.command(name="")
def cli(
    letter: str | None = None,
    style: NameStyle = typer.Option("title", help="Output format style."),
) -> None:
    """Generate a random Ubuntu-style name like 'Agile Amoeba'."""
    name = generate_name(letter, style=style)
    console.print(f"[bold red]{name}[/]")


if __name__ == "__main__":
    app()

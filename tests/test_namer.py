import string

import pytest

from ubuntu_namer import generate_name
from ubuntu_namer.__main__ import STYLES


def test_no_letter():
    name = generate_name()
    assert isinstance(name, str)
    assert len(name) > 0


def test_generate_all_letters():
    for letter in string.ascii_letters:
        name = generate_name(letter)
        assert isinstance(name, str)
        assert len(name) > 0


def test_digits_fail():
    for number in string.digits:
        with pytest.raises(AssertionError):
            generate_name(number)


def test_ints_fail():
    for number in range(10):
        with pytest.raises(ValueError):
            generate_name(number)


def test_multistring_fails():
    with pytest.raises(ValueError):
        generate_name("ab")


@pytest.mark.parametrize(
    "style, pattern",
    [
        ("title", r"^[A-Z][a-z]+ [A-Z][a-z]+$"),
        ("lower", r"^[a-z]+ [a-z]+$"),
        ("upper", r"^[A-Z]+ [A-Z]+$"),
        ("camel", r"^[a-z]+[A-Z][a-z]+$"),
        ("pascal", r"^[A-Z][a-z]+[A-Z][a-z]+$"),
        ("snake", r"^[a-z]+_[a-z]+$"),
        ("kebab", r"^[a-z]+-[a-z]+$"),
        ("dot", r"^[a-z]+\.[a-z]+$"),
    ],
)
def test_style_format(style, pattern):
    import re

    name = generate_name("a", style=style)
    assert re.match(pattern, name), f"style={style!r} produced {name!r}, expected {pattern}"


@pytest.mark.parametrize("letter", list(string.ascii_lowercase))
@pytest.mark.parametrize("style", STYLES)
def test_all_letters_all_styles(letter, style):
    name = generate_name(letter, style=style)
    assert isinstance(name, str)
    assert len(name) > 0
    assert name == name.strip()


def test_no_console_output(capsys):
    generate_name()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""


def test_invalid_style():
    with pytest.raises(ValueError, match="Unknown style"):
        generate_name(style="nonexistent")

import string

import pytest

from ubuntu_namer.main import generate_name


def test_no_letter():
    generate_name()


def test_generate_all_letters():
    for letter in string.ascii_letters:
        generate_name(letter)


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

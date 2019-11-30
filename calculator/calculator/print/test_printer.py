import pytest
from calculator.parse import parse_infix

from .printer import Printer


def print_test_helper(input: str, expected: str, capsys):
    Printer().print(parse_infix(input))
    out, __ = capsys.readouterr()
    assert out == expected


def test_printer_constant(capsys):
    print_test_helper("42", "42\n", capsys)


def test_printer_negated_constant(capsys):
    print_test_helper("-42", "-\n  42\n", capsys)


def test_printer_binaryop(capsys):
    print_test_helper("12 + 27", "+\n  12\n  27\n", capsys)


def test_print_complex_expression(capsys):
    print_test_helper(
        "12 + 27 * 42 ^51", "+\n  12\n  *\n    27\n    ^\n      42\n      51\n", capsys
    )

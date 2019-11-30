from calculator.ast import BinOp, Constant, UnaryOp
from calculator.core import operations

from .infix import parse_infix


def test_parse_constant():
    assert parse_infix("42") == Constant(42)


def test_parse_negated_constant():
    assert parse_infix("-42") == UnaryOp(operations.negate, Constant(42))


def test_parse_doubly_negated_constant():
    assert parse_infix("--42") == UnaryOp(
        operations.negate, UnaryOp(operations.negate, Constant(42))
    )


def test_parse_binary_operation():
    assert parse_infix("12 + 27") == BinOp(operations.plus, Constant(12), Constant(27))


def test_parse_complete_expression_tree():
    assert parse_infix("(12 + 27 )* (42 - 51)") == BinOp(
        operations.times,
        BinOp(operations.plus, Constant(12), Constant(27)),
        BinOp(operations.minus, Constant(42), Constant(51)),
    )


def test_power_binds_to_the_right():
    assert parse_infix("12 ^ 27 ^ 42") == BinOp(
        operations.pow, Constant(12), BinOp(operations.pow, Constant(27), Constant(42))
    )


def test_negate_and_pow_dont_mix():
    assert parse_infix("-12 ^ 27") == UnaryOp(
        operations.negate, BinOp(operations.pow, Constant(12), Constant(27))
    )

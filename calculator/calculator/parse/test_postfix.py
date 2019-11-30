from calculator.ast import BinOp, Constant, UnaryOp
from calculator.core import operations

from .postfix import parse_postfix


def test_parse_constant():
    assert parse_postfix("42") == Constant(42)


def test_parse_negated_constant():
    assert parse_postfix("42 @") == UnaryOp(operations.negate, Constant(42))


def test_parse_doubly_negated_constant():
    assert parse_postfix("42@@") == UnaryOp(
        operations.negate, UnaryOp(operations.negate, Constant(42))
    )


def test_parse_binary_operation():
    assert parse_postfix("12 27 +") == BinOp(
        operations.plus, Constant(12), Constant(27)
    )


def test_parse_complete_expression_tree():
    assert parse_postfix("12 27 + 42 51 - *") == BinOp(
        operations.times,
        BinOp(operations.plus, Constant(12), Constant(27)),
        BinOp(operations.minus, Constant(42), Constant(51)),
    )

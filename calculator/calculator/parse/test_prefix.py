from calculator.ast import BinOp, Constant, UnaryOp
from calculator.core import operations

from .prefix import parse_prefix


def test_parse_constant():
    assert parse_prefix("42") == Constant(42)


def test_parse_negated_constant():
    assert parse_prefix("@ 42") == UnaryOp(operations.negate, Constant(42))


def test_parse_doubly_negated_constant():
    assert parse_prefix("@@42") == UnaryOp(
        operations.negate, UnaryOp(operations.negate, Constant(42))
    )


def test_parse_binary_operation():
    assert parse_prefix("+ 12 27") == BinOp(operations.plus, Constant(12), Constant(27))


def test_parse_complete_expression_tree():
    assert parse_prefix("*+12 27-42 51") == BinOp(
        operations.times,
        BinOp(operations.plus, Constant(12), Constant(27)),
        BinOp(operations.minus, Constant(42), Constant(51)),
    )

import pytest
from calculator.ast import BinOp, Constant, UnaryOp
from calculator.core import operations

from .evaluator import Evaluator


@pytest.fixture
def vis():
    return Evaluator()


def test_evaluate_constant(vis):
    c = Constant(42)
    assert vis.visit_and_get_value(c) == 42


def test_evaluate_unaryop_identity(vis):
    op = UnaryOp(operations.identity, Constant(42))
    assert vis.visit_and_get_value(op) == 42


def test_evaluate_unaryop_negate(vis):
    op = UnaryOp(operations.negate, Constant(-42))
    assert vis.visit_and_get_value(op) == 42


def test_evaluate_binop_plus(vis):
    op = BinOp(operations.plus, Constant(12), Constant(27))
    assert vis.visit_and_get_value(op) == 39


def test_evaluate_binop_minus(vis):
    op = BinOp(operations.minus, Constant(42), Constant(51))
    assert vis.visit_and_get_value(op) == -9


def test_evaluate_binop_times(vis):
    op = BinOp(operations.times, Constant(6), Constant(9))
    assert vis.visit_and_get_value(op) == 54


def test_evaluate_binop_int_div(vis):
    op = BinOp(operations.int_div, Constant(5), Constant(2))
    assert vis.visit_and_get_value(op) == 2


def test_evaluate_binop_pow(vis):
    op = BinOp(operations.pow, Constant(3), Constant(4))
    assert vis.visit_and_get_value(op) == 81

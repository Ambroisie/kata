import pytest
from calculator.ast import BinOp, Constant, UnaryOp

from .evaluator import Evaluator


@pytest.fixture
def vis():
    return Evaluator()


def test_evaluate_constant(vis):
    c = Constant(42)
    assert vis.visit_and_get_value(c) == 42


def test_evaluate_unaryop_identity(vis):
    op = UnaryOp(lambda x: x, Constant(42))
    assert vis.visit_and_get_value(op) == 42


def test_evaluate_unaryop_negate(vis):
    op = UnaryOp(lambda x: -x, Constant(-42))
    assert vis.visit_and_get_value(op) == 42


def test_evaluate_binop_plus(vis):
    op = BinOp(lambda x, y: x + y, Constant(12), Constant(27))
    assert vis.visit_and_get_value(op) == 39


def test_evaluate_binop_minus(vis):
    op = BinOp(lambda x, y: x - y, Constant(42), Constant(51))
    assert vis.visit_and_get_value(op) == -9

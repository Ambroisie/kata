from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

from calculator.ast.visit import Visitor
from pydantic.dataclasses import dataclass

if TYPE_CHECKING:
    from calculator.ast import BinOp, Constant, Node, UnaryOp


@dataclass
class Evaluator(Visitor):
    """
    Evaluate a Tree and retrieve the calculated value.
    """

    value: int = dataclasses.field(default=0, init=False)

    def visit_and_get_value(self, n: Node) -> int:
        n.accept(self)
        return self.value

    def visit_constant(self, c: Constant) -> None:
        self.value = c.value

    def visit_binop(self, b: BinOp) -> None:
        lhs_val = self.visit_and_get_value(b.lhs)
        rhs_val = self.visit_and_get_value(b.rhs)
        self.value = b.op(lhs_val, rhs_val)

    def visit_unaryop(self, b: UnaryOp) -> None:
        rhs_val = self.visit_and_get_value(b.rhs)
        self.value = b.op(rhs_val)

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

from calculator.ast.visit import Visitor
from calculator.core.operations import (
    identity,
    int_div,
    minus,
    negate,
    plus,
    pow,
    times,
)
from pydantic.dataclasses import dataclass

if TYPE_CHECKING:
    from calculator.ast import BinOp, Constant, Node, UnaryOp

OP_TO_STR = {
    plus: "+",
    minus: "-",
    times: "*",
    int_div: "/",
    pow: "^",
    identity: "+",
    negate: "-",
}


@dataclass
class Printer(Visitor):
    """
    Print a Tree
    """

    indent: int = dataclasses.field(default=0, init=False)

    def print(self, n: Node) -> None:
        n.accept(self)

    def visit_constant(self, c: Constant) -> None:
        print(" " * self.indent + str(c.value))

    def visit_binop(self, b: BinOp) -> None:
        print(" " * self.indent + OP_TO_STR[b.op])
        self.indent += 2
        self.print(b.lhs)
        self.print(b.rhs)
        self.indent -= 2

    def visit_unaryop(self, b: UnaryOp) -> None:
        print(" " * self.indent + OP_TO_STR[b.op])
        self.indent += 2
        self.print(b.rhs)
        self.indent -= 2

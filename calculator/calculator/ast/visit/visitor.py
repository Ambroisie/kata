from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from calculator.ast import BinOp, Constant, Node, UnaryOp


class Visitor(ABC):
    """
    Abstract Visitor class for the AST class hierarchy.
    """

    def visit(self, n: Node) -> None:
        n.accept(self)

    @abstractmethod
    def visit_constant(self, c: Constant) -> None:
        pass

    @abstractmethod
    def visit_binop(self, b: BinOp) -> None:
        pass

    @abstractmethod
    def visit_unaryop(self, b: UnaryOp) -> None:
        pass

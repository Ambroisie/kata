from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from pydantic.dataclasses import dataclass

from .node import Node

if TYPE_CHECKING:
    from calculator.ast.visit import Visitor


class Config:
    arbitrary_types_allowed = True


@dataclass(config=Config)
class UnaryOp(Node):
    """
    Node to represent a unary operation
    """

    op: Callable[[int], int]
    rhs: Node

    def accept(self, v: Visitor) -> None:
        v.visit_unaryop(self)

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from pydantic.dataclasses import dataclass

from .node import Node

if TYPE_CHECKING:
    from calculator.ast.visit import Visitor


class Config:
    arbitrary_types_allowed = True


@dataclass(config=Config)
class BinOp(Node):
    """
    Node to represent a binary operation
    """

    op: Callable[[int, int], int]
    lhs: Node
    rhs: Node

    def accept(self, v: Visitor) -> None:
        v.visit_binop(self)

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

from .node import Node

if TYPE_CHECKING:
    from calculator.ast.visit import Visitor


class Config:
    arbitrary_types_allowed = True


@dataclass(config=Config)
class Constant(Node):
    """
    Node to represent a constant value.
    """

    value: int

    def accept(self, v: Visitor) -> None:
        v.visit_constant(self)

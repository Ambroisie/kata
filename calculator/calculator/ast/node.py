from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from calculator.ast.visit import Visitor


class Node(ABC):
    """
    Abstract Node class for calculator AST.
    """

    @abstractmethod
    def accept(self, v: Visitor) -> None:
        pass

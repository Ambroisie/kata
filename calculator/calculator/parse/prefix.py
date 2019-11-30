from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, cast

from calculator.ast import BinOp, Constant, UnaryOp
from calculator.core import operations

from .parsed_string import ParsedString

if TYPE_CHECKING:
    from calculator.ast import Node


def queue_to_tree(q: List[Union[int, str]]) -> Node:
    top = q.pop(0)
    if type(top) is int:
        return Constant(top)
    top = cast(str, top)
    if top == "@":
        rhs = queue_to_tree(q)
        return UnaryOp(operations.negate, rhs)
    lhs = queue_to_tree(q)
    rhs = queue_to_tree(q)
    return BinOp(operations.STR_TO_BIN[top], lhs, rhs)


def parse_prefix(input: str) -> Node:
    """
    Parses the given string in prefix notation.
    Negation is represented by the '@' sign.
    """
    parsed = ParsedString(input).tokenize()
    ans = queue_to_tree(parsed)
    return ans

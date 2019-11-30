from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, cast

from calculator.ast import BinOp, Constant, UnaryOp
from calculator.core import operations

from .parsed_string import ParsedString

if TYPE_CHECKING:
    from calculator.ast import Node


def stack_to_tree(s: List[Union[int, str]]) -> Node:
    top = s.pop()
    if type(top) is int:
        return Constant(top)
    top = cast(str, top)
    if top == "@":
        rhs = stack_to_tree(s)
        return UnaryOp(operations.negate, rhs)
    rhs = stack_to_tree(s)
    lhs = stack_to_tree(s)
    return BinOp(operations.STR_TO_BIN[top], lhs, rhs)


def parse_postfix(input: str) -> Node:
    """
    Parses the given string in postfix notation.
    Negation is represented by the '@' sign.
    """
    parsed = ParsedString(input).tokenize()
    ans = stack_to_tree(parsed)
    return ans

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, cast

from calculator.ast import BinOp, Constant, UnaryOp
from calculator.core import operations

from .parsed_string import ParsedString

if TYPE_CHECKING:
    from calculator.ast import Node


"""
E : T [ (+|-) T ]*

T : F [ (*|/) F ]*

F : [ (-|+) ]* P

P : G [ (^) F ]*

G : '(' E ')' | CONSTANT
"""


def parse_g(l: List[Union[int, str]]) -> Node:
    top = l.pop(0)
    if top == "(":
        ans = parse_e(l)
        assert l.pop(0) == ")"
        return ans
    return Constant(top)


def parse_p(l: List[Union[int, str]]) -> Node:
    lhs = parse_g(l)
    while len(l) and l[0] == "^":
        op = l.pop(0)
        rhs = parse_f(l)
        lhs = BinOp(operations.STR_TO_BIN[op], lhs, rhs)
    return lhs


def parse_f(l: List[Union[int, str]]) -> Node:
    str_to_unop = {
        "+": operations.identity,
        "-": operations.negate,
    }
    if l[0] in str_to_unop:
        op = l.pop(0)
        return UnaryOp(str_to_unop[op], parse_f(l))
    return parse_p(l)


def parse_t(l: List[Union[int, str]]) -> Node:
    lhs = parse_f(l)
    while len(l) and l[0] in ["*", "/"]:
        op = cast(str, l.pop(0))
        rhs = parse_t(l)
        lhs = BinOp(operations.STR_TO_BIN[op], lhs, rhs)
    return lhs


def parse_e(l: List[Union[int, str]]) -> Node:
    lhs = parse_t(l)
    while len(l) and l[0] in ["+", "-"]:
        op = cast(str, l.pop(0))
        rhs = parse_t(l)
        lhs = BinOp(operations.STR_TO_BIN[op], lhs, rhs)
    return lhs


def parse_infix(input: str) -> Node:
    """
    Parses the given string in infix notation.
    """
    parsed = ParsedString(input).tokenize()
    ans = parse_e(parsed)
    return ans

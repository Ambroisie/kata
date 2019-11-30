def plus(x: int, y: int) -> int:
    return x + y


def minus(x: int, y: int) -> int:
    return x - y


def times(x: int, y: int) -> int:
    return x * y


def int_div(x: int, y: int) -> int:
    return x // y


def pow(x: int, y: int) -> int:
    return x ** y


def identity(x: int) -> int:
    return x


def negate(x: int) -> int:
    return -x


STR_TO_BIN = {
    "+": plus,
    "-": minus,
    "*": times,
    "/": int_div,
    "^": pow,
}

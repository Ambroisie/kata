#! /usr/bin/env python
from typing import Callable, Dict


def fizzbuzzer(words: Dict[int, str]) -> Callable[[int], None]:
    def _fun(max: int) -> None:
        for i in range(1, max + 1):
            out = []
            for div, word in words.items():
                if i % div == 0:
                    out.append(word)
            if len(out) > 0:
                print("".join(out))
            else:
                print(i)

    return _fun


def fizzbuzz(max: int = 100) -> None:
    words = {
        3: "fizz",
        5: "buzz",
    }
    f = fizzbuzzer(words)
    f(max)


if __name__ == "__main__":
    fizzbuzz()

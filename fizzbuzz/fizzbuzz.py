#! /usr/bin/env python


def fizzbuzz(max: int = 100) -> None:
    words = {
        3: "fizz",
        5: "buzz",
    }
    for i in range(1, max + 1):
        out = []
        for div, word in words.items():
            if i % div == 0:
                out.append(word)
        if len(out) > 0:
            print("".join(out))
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz()

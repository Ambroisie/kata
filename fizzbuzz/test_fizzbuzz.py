from fizzbuzz import fizzbuzz


def list_output(max, capsys, expected_list):
    fizzbuzz(max)
    out, __ = capsys.readouterr()
    assert out == "\n".join(map(lambda x: str(x), expected_list)) + "\n"


def test_fizzbuzz_counts_to_two(capsys):
    list_output(2, capsys, [1, 2])


def test_fizzbuzz_shows_fizz_on_three(capsys):
    list_output(3, capsys, [1, 2, "fizz"])


def test_fizzbuzz_shows_buzz_on_five(capsys):
    list_output(5, capsys, [1, 2, "fizz", 4, "buzz"])


def test_fizzbuzz_shows_fizzbuzz_on_fifteen(capsys):
    list_output(
        15,
        capsys,
        [
            1,
            2,
            "fizz",
            4,
            "buzz",
            "fizz",
            7,
            8,
            "fizz",
            "buzz",
            11,
            "fizz",
            13,
            14,
            "fizzbuzz",
        ],
    )

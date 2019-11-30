from fizzbuzz import fizzbuzz, fizzbuzzer


def list_output(max, capsys, expected_list, function):
    function(max)
    out, __ = capsys.readouterr()
    assert out == "\n".join(map(lambda x: str(x), expected_list)) + "\n"


def list_fizzbuzz_output(max, capsys, expected_list):
    list_output(max, capsys, expected_list, fizzbuzz)


def test_fizzbuzz_counts_to_two(capsys):
    list_fizzbuzz_output(2, capsys, [1, 2])


def test_fizzbuzz_shows_fizz_on_three(capsys):
    list_fizzbuzz_output(3, capsys, [1, 2, "fizz"])


def test_fizzbuzz_shows_buzz_on_five(capsys):
    list_fizzbuzz_output(5, capsys, [1, 2, "fizz", 4, "buzz"])


def test_fizzbuzz_shows_fizzbuzz_on_fifteen(capsys):
    list_fizzbuzz_output(
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


def test_can_foobarbazz_customization(capsys):
    foobarbazz = fizzbuzzer({2: "foo", 3: "bar", 4: "bazz"})
    list_output(
        function=foobarbazz,
        max=12,
        capsys=capsys,
        expected_list=[
            1,
            "foo",
            "bar",
            "foobazz",
            5,
            "foobar",
            7,
            "foobazz",
            "bar",
            "foo",
            11,
            "foobarbazz",
        ],
    )


def test_can_foobarbazz_customization_regardless_of_dict_order(capsys):
    foobarbazz = fizzbuzzer({4: "bazz", 3: "bar", 2: "foo"})
    list_output(
        function=foobarbazz,
        max=12,
        capsys=capsys,
        expected_list=[
            1,
            "foo",
            "bar",
            "foobazz",
            5,
            "foobar",
            7,
            "foobazz",
            "bar",
            "foo",
            11,
            "foobarbazz",
        ],
    )

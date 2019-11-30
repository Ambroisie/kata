from fizzbuzz import fizzbuzz


def test_fizzbuzz_counts_to_two(capsys):
    fizzbuzz(2)
    out, __ = capsys.readouterr()
    assert out == "1\n2\n"

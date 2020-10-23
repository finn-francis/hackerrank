from append_and_delete import appendAndDelete

def test_same_string():
    odd_number_smaller = ("abc", "abc", 1)
    odd_number_bigger = ("abc", "abc", 7)
    even_number_smaller = ("abc", "abc", 2)
    even_number_bigger = ("abc", "abc", 10)

    assert appendAndDelete(*odd_number_smaller) == "No"
    assert appendAndDelete(*odd_number_bigger) == "Yes"
    assert appendAndDelete(*even_number_smaller) == "Yes"
    assert appendAndDelete(*even_number_bigger) == "Yes"

def test_add_string():
    smaller_correct = ("abcdef", "abc", 3)
    bigger_correct = ("abcdef", "abc", 9)
    smaller_incorrect = ("abcdef", "abc", 2)
    odd_bigger_diff = ("aaaaaaaaaa", "aaaaa", 7)

    assert appendAndDelete(*smaller_correct) == "Yes"
    assert appendAndDelete(*bigger_correct) == "Yes"
    assert appendAndDelete(*smaller_incorrect) == "No"
    assert appendAndDelete(*odd_bigger_diff) == "Yes"

def test_remove_string():
    smaller_correct = ("abc", "abcdef", 3)
    bigger_correct = ("abc", "abcdef", 9)
    smaller_incorrect = ("abc", "abcdef", 2)
    even_n_odd_diff = ("y", "yu", 2)
    odd_n_even_diff = ("y", "yuu", 3)

    assert appendAndDelete(*smaller_correct) == "Yes"
    assert appendAndDelete(*bigger_correct) == "Yes"
    assert appendAndDelete(*smaller_incorrect) == "No"
    assert appendAndDelete(*even_n_odd_diff) == "No"
    assert appendAndDelete(*odd_n_even_diff) == "No"

def test_remove_and_add():
    smaller_correct = ("abcefd", "abcdef", 6)
    bigger_correct = ("abcefd", "abcdef", 12)
    smaller_incorrect = ("abcefd", "abcdef", 5)

    assert appendAndDelete(*smaller_correct) == "Yes"
    assert appendAndDelete(*bigger_correct) == "Yes"
    assert appendAndDelete(*smaller_incorrect) == "No"

def test_empty_values():
    both_empty_zero = ("", "", 0)
    both_empty_even = ("", "", 2)
    both_empty_odd = ("", "", 1)

    assert appendAndDelete(*both_empty_zero) == "Yes"
    assert appendAndDelete(*both_empty_even) == "Yes"
    assert appendAndDelete(*both_empty_odd) == "Yes"

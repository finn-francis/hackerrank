from time_in_words import time_in_words

def test_on_the_hour():
    assert time_in_words(5, 0) == "five o' clock"

def test_1_minute_past():
    assert time_in_words(5, 1) == "one minute past five"

def test_x_minutes_past():
    assert time_in_words(5, 10) == "ten minutes past five"

def test_quarter_past():
    assert time_in_words(5, 15) == "quarter past five"

def test_half_past():
    assert time_in_words(5, 30) == "half past five"

def test_x_minutes_to():
    assert time_in_words(5, 35) == "twenty five minutes to six"

def test_quarter_to():
    assert time_in_words(5, 45) == "quarter to six"
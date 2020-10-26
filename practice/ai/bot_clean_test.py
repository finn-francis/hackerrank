from bot_clean import next_move

def test_1():
    floor = [
        ['b', '-', '-', '-', 'd'],
        ['-', 'd', '-', '-', 'd'],
        ['-', '-', 'd', 'd', '-'],
        ['-', '-', 'd', '-', '-'],
        ['-', '-', '-', '-', 'd']
    ]
    assert next_move(0, 0, floor) == "RIGHT"
    assert next_move(0, 1, floor) == "DOWN"
    assert next_move(1, 1, floor) == "CLEAN"

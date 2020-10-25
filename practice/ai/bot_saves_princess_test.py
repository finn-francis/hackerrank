from bot_saves_princess import save_princess

def test_1():
    grid = [
        ['-', '-', '-'],
        ['-', 'm', '-'],
        ['p', '-', '-']
    ]
    assert save_princess(grid) == "LEFT\nDOWN"

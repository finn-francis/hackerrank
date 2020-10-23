from organizing_containers_of_balls import organize_containers

def test_two_by_two_1():
    container = [[1, 1], [1, 1]]
    assert organize_containers(container, 2) == 'Possible'

def test_two_by_two_2():
    container = [[0, 2], [1, 1]]
    assert organize_containers(container, 2) == 'Impossible'

def test_three_by_three_1():
    container = [[1, 3, 1], [2, 1, 2], [3, 3, 3]]
    assert organize_containers(container, 3) == 'Impossible'

def test_three_by_three_2():
    container = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]
    assert organize_containers(container, 3) == 'Possible'
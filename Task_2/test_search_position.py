from search_position import find_position

def test_find_position():
    assert find_position([1, 2, 4, 4, 5, 6, 8], 4) == 2
    assert find_position([1, 2, 4, 4, 5, 6, 8], 7) == 6
    assert find_position([1, 2, 4, 4, 5, 6, 8], 9) == -1
    assert find_position([1, 2, 4, 4, 5, 6, 8], 0) == 0
    assert find_position([1, 2, 4, 4, 5, 6, 8], 5) == 4
    print("All test cases pass")

if __name__ == "__main__":
    test_find_position()

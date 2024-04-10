from src.find_if_path_exists.find_if_path_exists import Solution


s = Solution()


def test_create_graph():
    '''returns a dict, keys are nodes from 0 to n-1
       where n is the number of vertices.
       Values are lists containing the neighbors
       of the nodes which is the key'''
    expected_result = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }

    result = s.create_graph(3, [[0, 1], [1, 2], [2, 0]])
    for key in result:
        result[key].sort()

    assert result == expected_result


def test_validPath_same_source_and_destination():
    # Test case where source and destination are the same
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 0
    assert s.validPath(n, edges, source, destination)


def test_validPath_valid_path_exists():
    # Test case where a valid path exists from source to destination
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5
    assert not s.validPath(n, edges, source, destination)


def test_validPath_invalid_path():
    # Test case where no valid path exists from source to destination
    n = 6
    edges = [[1, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 2
    assert not s.validPath(n, edges, source, destination)

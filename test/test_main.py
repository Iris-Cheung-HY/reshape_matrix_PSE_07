from main.main import reshape_matrix
import pytest

def test_reshape_matrix_2_2():
    # arrange
    nums = [[1, 2],[3, 4]]
    rows = 1
    columns = 4
    
    result = reshape_matrix(nums, rows, columns)
    
    assert result == [[1, 2, 3, 4]]


def test_reshape_3_2():
    nums = [[1, 2],[3, 4],[5, 6]]
    rows = 2
    columns = 3
    
    result = reshape_matrix(nums, rows, columns)
    
    assert result == [[1, 2, 3], [4, 5, 6]]


def test_reshape_cannot_reshape():
    nums = [[1, 2], [3, 4]]
    rows = 2
    columns = 4
    
    with pytest.raises(ValueError):
        reshape_matrix(nums, rows, columns)


def test_reshpae_1_1():
    nums = [[1]]
    rows = 1
    columns = 1

    result = reshape_matrix(nums, rows, columns)
    
    assert result == [[1]]


def test_reshape_cannot_reshape_raise_message():
    nums = [[1, 2, 3], [4, 5, 6]]
    rows = 2
    columns = 4
    
    with pytest.raises(ValueError):
        reshape_matrix(nums, rows, columns)




def test_reshape_matrix_1_by_4_can_reshape_into_4_by_1():
    # Arrange
    nums = [[1], [2], [3], [4]]
    rows = 1
    columns = 4

    # Act
    result = reshape_matrix(nums, rows, columns)

    # Assert
    assert result == [[1, 2, 3, 4]]

def test_reshape_matrix_2_by_2_can_reshape_into_1_by_4():
    # Arrange
    nums = [[1, 2], [3, 4]]
    rows = 1
    columns = 4

    # Act
    result = reshape_matrix(nums, rows, columns)

    # Assert
    assert result == [[1, 2, 3, 4]]

def test_reshape_matrix_4_by_2_can_reshape_into_2_by_4():
    # Arrange
    nums = [[1, 2], [3, 4], [5, 6], [7, 8]]
    rows = 2
    columns = 4

    # Act
    result = reshape_matrix(nums, rows, columns)

    # Assert
    assert result == [[1, 2, 3, 4], [5, 6, 7, 8]]

def test_reshape_matrix_3_by_3_can_reshape_into_9_by_1():
    # Arrange
    nums = [[7, 2, 1], [4, 3, 5], [6, 9, 8]]
    rows = 9
    columns = 1 

    # Act
    result = reshape_matrix(nums, rows, columns)

    # Assert
    assert result == [[7], [2], [1], [4], [3], [5], [6], [9], [8]]

def test_reshape_matrix_2_by_2_raises_error_reshaping_to_4_by_2():
    # Arrange
    nums = [[1,2], [3,4]]
    rows = 4
    columns = 2

    # Act & Assert
    with pytest.raises(ValueError):
        reshape_matrix(nums, rows, columns)
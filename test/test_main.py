from main.main import reshape_matrix

def test_reshape_matrix_2_2(nums, rows, columns):
    # arrange
    nums = 
    [[1, 2],
    [3, 4]]
    rows = 1
    columns = 4
    
    result = reshape_matrix(nums, rows, columns)
    
    assert result == [[1, 2, 3, 4]]
    
def test_reshape_rows_error(nums, rows, columns):
    nums = 
    [[1, 2],
    [3, 4]]
    rows = 2
    columns = 4
    
    result = reshape_matrix(nums, rows, columns)
    
    with pytest.raises(ValueError, match="Matrix cannot reshape"):
        reshape_matrix(nums, rows, columns)


def test_reshape_rows_error(nums, rows, columns):
    nums = 
    [[1, 2],
    [3, 4],
    [5, 6]]
    rows = 2, columns = 3
    
    result = reshape_matrix(nums, rows, columns)
    
    assert result == [[1, 2, 3], [4, 5, 6]]

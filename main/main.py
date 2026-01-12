def reshape_matrix(nums, rows, columns):
    flat_mat = []
    new_matrix = []


    for r in nums:
        for item in r:
            flat_mat.append(item)
    
    if rows * columns != len(flat_mat):
        raise ValueError

    l = 0
    while len(new_matrix) < rows:
        new_matrix.extend([flat_mat[l : l + columns]])
        l += columns

    return new_matrix















































#     new_shape = []
#     temp_list = []

#     for matrix in nums:
#         for n in matrix:
#             temp_list.append(n)
    
#     if check_valid(temp_list, rows, columns):
#         run = 0
#         start = 0
#         while run != rows:
#             row_nums = temp_list[start: start + columns]
#             new_shape.append(row_nums)
#             start += columns
#             run += 1
#         return new_shape


# def check_valid(temp_list, rows, columns):
#     if len(temp_list) != rows * columns:
#         raise ValueError("Matrix cannot reshape")
#     return True


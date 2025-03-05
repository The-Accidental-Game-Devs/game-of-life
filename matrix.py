
def get_neighbouring_cell(matrix, row, col):
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
        (-1, 1),  # Top-right
        (1, -1),  # Bottom-left
        (-1, -1), # Top-left
        (1, 1),   # Bottom-right
    ]

    rows, cols = len(matrix), len(matrix[0])
    neighbours = []

    for dr, dc in directions:
        next_row, next_col = row + dr, col + dc

        if not is_index_out_of_range(next_row, next_col, rows, cols):
            neighbours.append(matrix[next_row][next_col])

    return neighbours

def is_index_out_of_range(row_index, col_index, row_size, col_size) -> bool:
    return not (0 <= row_index < row_size and 0 <= col_index < col_size)

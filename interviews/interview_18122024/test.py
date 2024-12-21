def is_valid_move(x, y, rows, cols):
    """Check if the cell (x, y) is within matrix bounds."""
    return 0 <= x < rows and 0 <= y < cols


def search_in_direction(matrix, word, start_x, start_y, direction_x, direction_y):
    """Search for the word starting from (start_x, start_y) in a specific direction."""
    rows, cols = len(matrix), len(matrix[0])
    for i in range(len(word)):
        new_x = start_x + i * direction_x
        new_y = start_y + i * direction_y

        if not is_valid_move(new_x, new_y, rows, cols) or matrix[new_x][new_y] != word[i]:
            return False
    return True


def search_word(matrix, word):
    """Search for the word in the matrix."""
    rows, cols = len(matrix), len(matrix[0])

    # Possible directions: right, left, down, up, diagonals
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == word[0]:  # First letter matches
                for direction_x, direction_y in directions:
                    if search_in_direction(matrix, word, x, y, direction_x, direction_y):
                        return "Word is available"
    return "Word is not available"


# Example usage
matrix = [
    ['W', 'O', 'R', 'D'],
    ['X', 'S', 'E', 'A'],
    ['Y', 'C', 'H', 'N'],
    ['Z', 'B', 'A', 'D']
]

word = "WORD"  # Input word
result = search_word(matrix, word)
print(result)  # Output: "Word is available"

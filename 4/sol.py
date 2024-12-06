import sys
import re

infile = sys.argv[1] if len(sys.argv)>=2 else '/Users/hitajuneja/Documents/GitHub/adventofcode2024/4/input.txt'
grid = open(infile).read().strip().split('\n')
print(len(grid)) 
print(len(grid[0])) 
print(type(grid)) 
print(type(grid[0])) 

def find_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    occurrences = {
        'horizontal': 0,
        'vertical': 0,
        'diagonal': 0,
        'reverse_diagonal': 0,
        'backward': 0
    }

    # Horizontal and Backward Search
    for row in grid:
        row_str = ''.join(row)  # Join the row list into a string
        occurrences['horizontal'] += len(re.findall(f'{word}', row_str))  # Forward horizontal
        occurrences['backward'] += len(re.findall(f'{word[::-1]}', row_str))  # Backward horizontal

    # Vertical and Backward Vertical Search
    for col in range(cols):
        column_str = ''.join([grid[row][col] for row in range(rows)])  # Join column into a string
        occurrences['vertical'] += len(re.findall(f'{word}', column_str))  # Forward vertical
        occurrences['backward'] += len(re.findall(f'{word[::-1]}', column_str))  # Backward vertical

    # Diagonal Search (Top-left to Bottom-right)
    for diag in range(-rows + 1, cols):  # Range of diagonals
        diagonal_str = ''.join(
            [grid[row][col] for row in range(rows) for col in range(cols) if row - col == diag]
        )
        occurrences['diagonal'] += len(re.findall(f'{word}', diagonal_str))  # Forward diagonal
        occurrences['reverse_diagonal'] += len(re.findall(f'{word[::-1]}', diagonal_str))  # Reverse diagonal

    # Reverse Diagonal Search (Top-right to Bottom-left)
    for diag in range(rows + cols - 1):
        reverse_diagonal_str = ''.join(
            [grid[row][col] for row in range(rows) for col in range(cols) if row + col == diag]
        )
        occurrences['diagonal'] += len(re.findall(f'{word}', reverse_diagonal_str))  # Forward reverse diagonal
        occurrences['reverse_diagonal'] += len(re.findall(f'{word[::-1]}', reverse_diagonal_str))  # Reverse reverse diagonal

    return occurrences


word = 'XMAS'

# Get the occurrences
occurrences = find_occurrences(grid, word)

# Print the results
print(f"Horizontal Occurrences: {occurrences['horizontal']}")
print(f"Vertical Occurrences: {occurrences['vertical']}")
print(f"Diagonal Occurrences: {occurrences['diagonal']}")
print(f"Reverse Diagonal Occurrences: {occurrences['reverse_diagonal']}")
print(f"Backward Occurrences: {occurrences['backward']}")

print(occurrences['horizontal'] + occurrences['vertical'] + occurrences['diagonal'] + occurrences['reverse_diagonal'] + occurrences['backward'])


def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Function to check if a string matches "MAS" or "SAM"
    def matches_mas(s):
        return s == "MAS" or s == "SAM"

    # Check for the X-MAS pattern
    for r in range(1, rows - 1):  # Skip the first and last row
        for c in range(1, cols - 1):  # Skip the first and last column
            # Check top-left to bottom-right diagonal
            top_left = "".join([grid[r - 1][c - 1], grid[r][c], grid[r + 1][c + 1]])
            # Check top-right to bottom-left diagonal
            top_right = "".join([grid[r - 1][c + 1], grid[r][c], grid[r + 1][c - 1]])

            if matches_mas(top_left) and matches_mas(top_right):
                count += 1

    return count

print(count_x_mas(grid))
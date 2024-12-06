import sys

infile = sys.argv[1] if len(sys.argv)>=2 else '/Users/hitajuneja/Documents/GitHub/adventofcode2024/6/input.txt'
grid = open(infile).read().strip()
grid = [list(line) for line in grid.splitlines()]

# print(grid)
pos_row, pos_col = None, None
guard = None  

# Find the guard's starting position
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] in ('^', 'v', '<', '>'):
            pos_row, pos_col = r, c
            guard = grid[r][c] 
            break
    if pos_row is not None:
        break    

print(pos_row, pos_col, guard)

def reached_edge_of_matrix(pos_row, pos_col, grid):
    if pos_row == 0 or pos_row == len(grid) - 1 or pos_col == 0 or pos_col == len(grid[0]) - 1:
        return True
    return False

while True:
    if reached_edge_of_matrix(pos_row, pos_col, grid):
        grid[pos_row][pos_col] = 'X'
        break
    elif grid[pos_row - 1][pos_col] == '#' and movement == 'up':
        guard = '>'
        movement = 'right'
        grid[pos_row][pos_col] = 'X'
        pos_col += 1
        print(pos_row, pos_col, guard) 
    elif grid[pos_row +1 ][pos_col] == '#' and movement == 'down':
        guard = '<'
        movement = 'left'
        grid[pos_row][pos_col] = 'X'
        pos_col -= 1 
        print(pos_row, pos_col, guard) 

    elif grid[pos_row][pos_col - 1] == '#' and movement == 'left':
        guard = '^'
        movement = 'up'
        grid[pos_row][pos_col] = 'X'
        pos_row-=1
        print(pos_row, pos_col, guard) 

    elif grid[pos_row][pos_col + 1] == '#' and movement == 'right':
        guard = 'v'
        movement = 'down'
        grid[pos_row][pos_col] = 'X'
        pos_row+=1
        print(pos_row, pos_col, guard) 

    else:
        grid[pos_row][pos_col] = 'X'
        if guard == '^':
            pos_row-=1
        elif guard == 'v':
            pos_row+=1
        elif guard == '<':
            pos_col-=1
        elif guard == '>':
            pos_col+=1

count = 0
for row in grid:
    for col in row:
        if col == 'X':
            count+=1
        print(col, end='')
    print()
    
print(count)
import sys

infile = sys.argv[1] if len(sys.argv)>=2 else '/Users/hitajuneja/Documents/GitHub/adventofcode2024/2/input.txt'
D = open(infile).read().strip()

rows = D.split('\n')
grid = [list(map(int, row.split(' '))) for row in rows]

safe = 0

def is_safe(report):
    """Checks if a report is safe."""
    if report == sorted(report) or report == sorted(report, reverse=True):
        for i in range(len(report) - 1):
            if abs(report[i] - report[i + 1]) > 3 or report[i] == report[i + 1]:
                return False
        return True
    return False

for row in grid:
    if is_safe(row):
        safe += 1
    else:
        for i in range(len(row)):
            new_row = row[:i] + row[i + 1:]  # Remove the i-th level
            if is_safe(new_row):
                safe += 1
                break  # Only count once if it becomes safe after removing one level

print(safe)

    
import sys
from collections import Counter

infile = sys.argv[1] if len(sys.argv)>=2 else '/Users/hitajuneja/Documents/GitHub/adventofcode2024/1/input.txt'
D = open(infile).read().strip()

rows = D.split('\n')

left = []
right =[]
s=0
for row in rows:
    l, r = row.split()
    l, r = int(l), int(r)
    left.append(l)
    right.append(r)
    print(row)

left = sorted(left)
right = sorted(right)


for l,r in zip(left,right):
    s += abs(r-l)
print(s)

# Precompute the count of each element in `right`
right_count = Counter(right)

score = 0
for i in left:
    # Get the count of `i` in `right` (or 0 if it doesn't exist)
    c = right_count.get(i, 0)
    score += i * c

print(score)
    
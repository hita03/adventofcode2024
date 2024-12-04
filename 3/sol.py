import sys
import re as regex

infile = sys.argv[1] if len(sys.argv)>=2 else '/Users/hitajuneja/Documents/GitHub/adventofcode2024/3/input.txt'
string = open(infile).read().strip()
# print(string)

enabled = True
to_multiply = []
mul=0

# part1
to_multiply = regex.findall(r"mul\(\d+,\s*\d+\)", string)
print(to_multiply)
for i in to_multiply:
    i = i.replace('mul', "")
    i = i.replace(')', "")
    i = i.replace('(', "")
    mul += int(i.split(',')[0]) * int(i.split(',')[1])
        
print(mul)

# part2
index = 0
mul = 0
while index < len(string):
    match = regex.match(r'mul\((\d{1,3}),(\d{1,3})\)', string[index:])
    if string[index:].startswith("do()"):
        enabled = True
    if string[index:].startswith("don't()"):
        enabled = False
    
    if match is not None and enabled:
        x,y = int(match.group(1)), int(match.group(2))
        mul += x*y
    index += 1
        
print(mul)

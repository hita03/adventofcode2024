import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else '/Users/hitajuneja/Documents/GitHub/adventofcode2024/5/input.txt'
rules, updates = open(infile).read().strip().split('\n\n')

rules = [[int(num) for num in line.split('|')] for line in rules.splitlines()]
updates = [[int(num) for num in line.split(',')] for line in updates.splitlines()]


s = 0

def is_update_valid(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            index_0 = update.index(rule[0])
            index_1 = update.index(rule[1])
            
            if index_0 > index_1:
                return False 
    return True 

def update_sum(row, s):
    middle_element = row[len(row) // 2] 
    return s + middle_element

for update in updates:
    if is_update_valid(update, rules):
        s = update_sum(update, s)

print(s)

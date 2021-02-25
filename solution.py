string = "3+12+(3+6*9)+31*7"

def func(line):
    stack = []

    if line[0] == '(' and line[-1] == ')':
        exp = line[1: -1]


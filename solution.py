string = "((2+3*6)+(2-3)*6)/(7+2)"


def check_global_brackets(line):
    length = len(line)

    stack = []

    for i in range(length):
        if line[i] == '(':
            stack.append(0)
        elif line[i] == ')':
            stack.pop()
            if len(stack) == 0:
                if i == length - 1:
                    return True
                else:
                    return False


class Node:
    def __init__(self, value):
        self.core = value
        self.right = None
        self.left = None

    def insert(self, node, direction_right):
        if direction_right:
            self.right = node
        else:
            self.left = node

    def apply(self):
        if self.core.isdigit():
            return self.core

        return self.left.apply() + self.right.apply() + self.core


def iterate(line, stack, oper1, oper2):
    for i in reversed(range(len(line))):
        ch = line[i]

        if ch == ')':
            stack.append(0)
        if ch == '(':
            stack.pop()

        if len(stack) == 0 and (ch == oper1 or ch == oper2):
            node = Node(ch)

            node.insert(func(line[:i]), False)
            node.insert(func(line[i + 1:]), True)

            return node

    return False


def func(line):
    stack = []

    if line[0] == '(' and line[-1] == ')':
        if check_global_brackets(line):
            line = line[1: -1]

    result_node = iterate(line, stack, "+", "-")
    if result_node:
        return result_node

    result_node = iterate(line, stack, "*", "/")
    if result_node:
        return result_node

    return Node(line) #is leaf


print(func(string).apply())

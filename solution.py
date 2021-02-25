string = "((3*7)/5*6*3)"

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
    for i in range(len(line)):
        ch = line[i]

        if ch == '(':
            stack.append(0)
        if ch == ')':
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
        line = line[1: -1]

    result_node = iterate(line, stack, "+", "-")
    if result_node:
        return result_node

    result_node = iterate(line, stack, "*", "/")
    if result_node:
        return result_node

    return Node(line) #is leaf


print(func(string).apply())

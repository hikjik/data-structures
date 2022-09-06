# 69744416

import operator
from typing import List

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


class PopFromEmptyStackError(Exception):
    pass


class Stack:
    def __init__(self) -> None:
        self._items: List[int] = []

    def push(self, item: int) -> None:
        self._items.append(item)

    def pop(self) -> int:
        if not self._items:
            raise PopFromEmptyStackError
        return self._items.pop()


def read_input() -> List[str]:
    return input().split()


def calculate(items: List[str]) -> int:
    stack = Stack()
    for item in items:
        if item in OPERATIONS:
            operation = OPERATIONS[item]
            a, b = stack.pop(), stack.pop()
            stack.push(operation(b, a))
        else:
            stack.push(int(item))
    return stack.pop()


if __name__ == "__main__":
    items = read_input()
    print(calculate(items))

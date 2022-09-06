# 69744415

from dataclasses import dataclass
from typing import List, Tuple


class OverflowDequeError(Exception):
    pass


class PopFromEmptyDequeError(Exception):
    pass


class Deque:
    def __init__(self, maxlen: int) -> None:
        self._items = [0] * maxlen
        self._maxlen = maxlen
        self._size = 0
        self._head = 0
        self._tail = -1

    def push_back(self, item: int) -> None:
        if self._size == self._maxlen:
            raise OverflowDequeError

        self._tail = (self._tail + 1) % self._maxlen
        self._items[self._tail] = item
        self._size += 1

    def push_front(self, item: int) -> None:
        if self._size == self._maxlen:
            raise OverflowDequeError

        self._head = (self._head - 1) % self._maxlen
        self._items[self._head] = item
        self._size += 1

    def pop_back(self) -> int:
        if self._size == 0:
            raise PopFromEmptyDequeError

        item = self._items[self._tail]
        self._tail = (self._tail - 1) % self._maxlen
        self._size -= 1
        return item

    def pop_front(self) -> int:
        if self._size == 0:
            raise PopFromEmptyDequeError

        item = self._items[self._head]
        self._head = (self._head + 1) % self._maxlen
        self._size -= 1
        return item


@dataclass
class Command:
    name: str
    args: List[int]


def parse_command(item: str) -> Command:
    name, *args = item.split()
    return Command(
        name=name,
        args=[int(a) for a in args],
    )


def read_input() -> Tuple[int, List[Command]]:
    count = int(input())
    maxlen = int(input())

    commands = [parse_command(input()) for _ in range(count)]

    return maxlen, commands


def process(maxlen: int, commands: List[Command]) -> List[str]:
    deque = Deque(maxlen)

    results: List[str] = []
    for command in commands:
        try:
            value = getattr(deque, command.name)(*command.args)
            if value is not None:
                results.append(str(value))
        except (OverflowDequeError, PopFromEmptyDequeError):
            results.append("error")
    return results


if __name__ == "__main__":
    maxlen, commands = read_input()
    results = process(maxlen, commands)
    print("\n".join(results))

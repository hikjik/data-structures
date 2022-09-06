from typing import List, Optional


class Stack:
    def __init__(self) -> None:
        self._items: List[int] = []
        self._maximums: List[int] = []

    def push(self, item: int) -> None:
        if self._maximums:
            self._maximums.append(max(item, self._maximums[-1]))
        else:
            self._maximums.append(item)

        self._items.append(item)

    def pop(self) -> None:
        self._items.pop()
        self._maximums.pop()

    def get_max(self) -> Optional[int]:
        return self._maximums[-1] if self._maximums else None


if __name__ == "__main__":
    rows = int(input())
    stack = Stack()
    for i in range(rows):
        command = input()
        if command.startswith("pop"):
            try:
                stack.pop()
            except IndexError:
                print("error")
        elif command.startswith("push"):
            item = int(command.strip().split()[1])
            stack.push(item)
        elif command.startswith("get_max"):
            print(stack.get_max())
        else:
            print(f"Unknown command {command}")

import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def put(self, x):
        if not self.head:
            self.tail = self.head = Node(x)
        else:
            node = Node(x)
            self.tail.next = node
            self.tail = node
        self.size += 1

    def get(self):
        if self.size == 0:
            return "error"
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value


if __name__ == "__main__":
    rows = int(input())
    queue = Queue()

    for i in range(rows):
        command = input()
        if command.startswith("get"):
            sys.stdout.write(queue.get() + "\n")
        elif command.startswith("put"):
            queue.put(command.split()[1])
        elif command.startswith("size"):
            sys.stdout.write(str(queue.size) + "\n")
        else:
            print(f"Unknown command {command}")

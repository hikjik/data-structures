import io
import os
import sys


class QueueSized:
    def __init__(self, cap):
        self.queue = [None] * cap
        self.cap = cap
        self.head = 0
        self.tail = 0
        self.size = 0

    def empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.cap:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.cap
            self.size += 1

    def peek(self):
        if self.empty():
            return str(None)
        return self.queue[self.head]

    def pop(self):
        if self.empty():
            return str(None)
        x = self.queue[self.head]
        self.head = (self.head + 1) % self.cap
        self.size -= 1
        return x


if __name__ == "__main__":
    rows, cap = int(input()), int(input())
    queue = QueueSized(cap)

    for i in range(rows):
        command = input()
        if command.startswith("peek"):
           sys.stdout.write(queue.peek() + "\n")
        elif command.startswith("push"):
            if queue.size == queue.cap:
                sys.stdout.write("error\n")
            else:
                item = command.split()[1]
                queue.push(item)
        elif command.startswith("size"):
            sys.stdout.write(str(queue.size) + "\n")
        elif command.startswith("pop"):
            sys.stdout.write(queue.pop() + "\n")
        else:
            print(f"Unknown command {command}")

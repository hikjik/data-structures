import sys


def open(closed):
    if closed == "}":
        return "{"
    if closed == ")":
        return "("
    if closed == "]":
        return "["


def is_correct_bracket_seq() -> bool:
    opened = ["{", "[", "("]
    closed = ["}", "]", ")"]

    stack = []
    while True:
        s = sys.stdin.read(1)
        if s in opened:
            stack.append(s)
        elif s in closed:
            if not stack or open(s) != stack[-1]:
                return False
            stack.pop()
        else:
            return len(stack) == 0


if __name__ == "__main__":
    print(is_correct_bracket_seq())

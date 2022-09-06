def fib(k: int) -> int:
    if k < 2:
        return 1
    return fib(k - 1) + fib(k - 2)


if __name__ == "__main__":
    k = int(input())
    print(fib(k))
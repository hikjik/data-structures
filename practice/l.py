def fib(n: int, k: int) -> int:
    if n < 2:
        return 1

    a, b = 1, 1
    m = 10**k

    for _ in range(n - 1):
        a, b = b, (a + b) % m

    return b


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(fib(n, k))

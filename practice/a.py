if __name__ == "__main__":
    n, m = int(input()), int(input())

    matrix = [input().split() for _ in range(n)]

    for j in range(m):
        for i in range(n):
            print(matrix[i][j], end=" ")
        print()

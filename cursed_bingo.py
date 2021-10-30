def bingo(n: int) -> int:
    return n * (n - 1)


if __name__ == "__main__":
    L = int(input())
    for _ in range(L):
        N = int(input())
        print(bingo(N))

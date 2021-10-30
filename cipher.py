if __name__ == "__main__":
    n_cols = int(input())
    col_order = map(int, input().split())
    message = input()
    n = len(message)
    for col in col_order:
        i = col - 1
        while i < n:
            print(message[i], end="")
            i += n_cols
    print()

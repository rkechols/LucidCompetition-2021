if __name__ == "__main__":
    m = int(input())
    counts = dict()
    for _ in range(m):
        num = int(input())
        try:
            counts[num] += 1
        except KeyError:
            counts[num] = 1
    max_count = max(counts.values())
    print(max_count > (m * 2 / 3))

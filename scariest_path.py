if __name__ == "__main__":
    n = int(input())
    scariness = list(map(int, input().split()))
    adjacency_matrix = list()
    for _ in range(n):
        adjacency_matrix.append(list(map(lambda x: x == "1", input().split())))
    print('hi')

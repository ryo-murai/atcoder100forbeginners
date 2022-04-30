import itertools


def find(n, x):
    result = []
    for n1, n2, n3 in itertools.combinations(range(1, n + 1), 3):
        if n1 + n2 + n3 == x:
            result.append((n1, n2, n3))
    print(f"{len(result)}")


while True:
    n, x = map(int, input().split(" "))
    if n == 0 and x == 0:
        break
    find(n, x)

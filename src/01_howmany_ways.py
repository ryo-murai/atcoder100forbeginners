def find(n, x):
    result = []
    for n1 in range(1, n - 1):
        for n2 in range(n1 + 1, n):
            for n3 in range(n2 + 1, n + 1):
                # print(f"{n1} {n2} {n3}")
                if n1 + n2 + n3 == x:
                    result.append((n1, n2, n3))
                    # print(f"{n1} {n2} {n3}")
    print(f"{len(result)}")


while True:
    (nx, xx) = input().split((" "))
    (n, x) = int(nx), int(xx)
    if n == 0 and x == 0:
        break
    find(n, x)

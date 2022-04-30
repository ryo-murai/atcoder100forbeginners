NUM_DENOM = 8


def count_denom(n):
    count = 0
    for d in range(1, n + 1):
        if n % d == 0:
            count = count + 1
            if count > NUM_DENOM:
                break
    return count


result = []
nx = int(input())
for n in range(1, nx + 1):
    if n % 2 != 0 and count_denom(n) is NUM_DENOM:
        result.append(n)

print(len(result))

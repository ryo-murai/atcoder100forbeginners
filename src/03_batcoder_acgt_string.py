def len_acgt(s: str):
    max = 0
    curr = 0
    for c in s:
        if c in "ACGT":
            curr = curr + 1
            if curr > max:
                max = curr
        else:
            curr = 0
    return max


print(len_acgt(input()))

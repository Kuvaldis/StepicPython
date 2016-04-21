def compound(n, k):
    if (k == 0):
        return 1
    elif (k > n):
        return 0
    return compound(n - 1, k) + compound(n - 1, k - 1)
n, k = map(int, input().split())
print(compound(n, k))

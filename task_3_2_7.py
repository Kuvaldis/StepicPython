def entries(s, t):
    return len(list(filter(lambda x: x, [s.startswith(t, start) for start in range(0, len(s) - len(t) + 1)])))

print(entries("abababa", "aba"))

def check(s, a, b):
    res = 0
    while True:
        if not a in s:
            return res
        new_s = s.replace(a, b)
        if s == new_s:
            return "Impossible"
        s = new_s
        res += 1
        if res > 100:
            return "Impossible"


print(check("ababa", "a", "b"))
print(check("ababa", "b", "a"))
print(check("ababa", "c", "c"))
print(check("ababac", "c", "c"))

print(check(input(), input(), input()))

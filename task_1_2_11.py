objects = [1, 2, 1, 2, 3]
ans = 0
ids = set()
for obj in objects:
  ans += 1 if id(obj) not in ids else 0
  ids.add(id(obj))
print(ans)

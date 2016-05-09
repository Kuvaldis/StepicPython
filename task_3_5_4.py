import json

# j = input()
j = """
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
"""

loaded = json.loads(j)
up_hier = dict()
hier = dict()
for desc in loaded:
    hier[desc['name']] = set()
    up_hier[desc['name']] = desc['parents']


def propagate(name, parents):
    for parent in parents:
        hier[parent].add(name)
        propagate(name, up_hier[parent])


for pair in up_hier.items():
    propagate(pair[0], pair[1])
print("\n".join(sorted([key + ' : ' + str(len(value) + 1) for key, value in hier.items()])))

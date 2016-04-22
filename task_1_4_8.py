namespaces = {"global": {"parent": None, "variables": []}}

def add_namespace(namespace, parent):
    namespaces[namespace] = {"parent": parent, "variables": []} 

def add_var(namespace, var):
    namespaces[namespace]["variables"].append(var)

def get_var(namespace, var):
    current_namespace = namespace
    while current_namespace in namespaces:
        if var in namespaces[current_namespace]["variables"]:
            return current_namespace
        current_namespace = namespaces[current_namespace]["parent"]
    return None

request_number = int(input())
for _ in range(request_number):
    request_parts = input().split(" ")
    command = request_parts[0]
    namespace = request_parts[1]
    if command == "create":
        parent = request_parts[2]
        add_namespace(namespace, parent)
    elif command == "add":
        var = request_parts[2]
        add_var(namespace, var)
    elif command == "get":
        var = request_parts[2]
        print(get_var(namespace, var))

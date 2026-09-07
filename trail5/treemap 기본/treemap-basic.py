n = int(input())

cmd = []
k = []
v = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] == "add":
        k.append(int(line[1]))
        v.append(int(line[2]))
    elif line[0] == "remove" or line[0] == "find":
        k.append(int(line[1]))
        v.append(0)
    else:
        k.append(0)
        v.append(0)

# Please write your code here.
treemap = {}
output = []

for i in range(n):
    c = cmd[i]
    if c == "add":
        treemap[k[i]] = v[i]
    elif c == "remove":
        if k[i] in treemap:
            del treemap[k[i]]
    elif c == "find":
        if k[i] in treemap:
            output.append(str(treemap[k[i]]))
        else:
            output.append("None")
    elif c == "print_list":
        if len(treemap) == 0:
            output.append("None")
        else:
            sorted_keys = sorted(treemap.keys())
            values = [str(treemap[key]) for key in sorted_keys]
            output.append(" ".join(values))

print("\n".join(output))
n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Please write your code here.
hashmap = {}
output = []

for command in commands:
    cmd = command[0]
    k = command[1]
    if cmd == "add":
        v = command[2]
        hashmap[k] = v
    elif cmd == "remove":
        if k in hashmap:
            del hashmap[k]
    elif cmd == "find":
        if k in hashmap:
            output.append(str(hashmap[k]))
        else:
            output.append("None")

print("\n".join(output))
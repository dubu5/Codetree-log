from collections import deque
N, G = map(int, input().split())

group = []
group_size = []

for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(nums[1:])

# Please write your code here.
person_groups = [[] for _ in range(N + 1)]
for i in range(G):
    for p in group[i]:
        person_groups[p].append(i)

remaining = group_size[:]
invited = [False] * (N + 1)
queue = deque()

def invite(p):
    if not invited[p]:
        invited[p] = True
        queue.append(p)

def check_group(gi):
    if remaining[gi] == 1:
        for q in group[gi]:
            if not invited[q]:
                invite(q)
                break

for gi in range(G):
    check_group(gi)

invite(1)

while queue:
    p = queue.popleft()
    for gi in person_groups[p]:
        remaining[gi] -= 1
        check_group(gi)

print(sum(invited))
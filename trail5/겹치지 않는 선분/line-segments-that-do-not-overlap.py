n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

lines.sort()

left_max = [float('-inf')] * n
curr_max = float('-inf')
for i in range(n):
    left_max[i] = curr_max
    if lines[i][1] > curr_max:
        curr_max = lines[i][1]

right_min = [float('inf')] * n
curr_min = float('inf')
for i in range(n - 1, -1, -1):
    right_min[i] = curr_min
    if lines[i][1] < curr_min:
        curr_min = lines[i][1]

ans = 0
for i in range(n):
    if left_max[i] < lines[i][1] < right_min[i]:
        ans += 1

print(ans)
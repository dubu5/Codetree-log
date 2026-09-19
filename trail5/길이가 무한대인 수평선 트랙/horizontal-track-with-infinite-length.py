n, t = map(int, input().split())
start = []
speed = []

for _ in range(n):
    s, v = map(int, input().split())
    start.append(s)
    speed.append(v)

groups = 0
min_final_pos = float('inf')

for i in range(n - 1, -1, -1):
    expected_pos = start[i] + speed[i] * t
    
    if expected_pos < min_final_pos:
        groups += 1
        min_final_pos = expected_pos

print(groups)
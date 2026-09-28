import sys

input = sys.stdin.readline

n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

points.sort()
point_to_idx = {val: idx for idx, val in enumerate(points)}

for a, b in queries:
    print(point_to_idx[b] - point_to_idx[a] + 1)
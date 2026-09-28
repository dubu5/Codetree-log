import sys
import bisect

input = sys.stdin.readline

n, q = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]

x_vals = sorted(list(set([p[0] for p in points])))
y_vals = sorted(list(set([p[1] for p in points])))

nx = len(x_vals)
ny = len(y_vals)

grid = [[0] * (ny + 1) for _ in range(nx + 1)]

for x, y in points:
    cx = bisect.bisect_left(x_vals, x) + 1
    cy = bisect.bisect_left(y_vals, y) + 1
    grid[cx][cy] += 1

for i in range(1, nx + 1):
    for j in range(1, ny + 1):
        grid[i][j] += grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1]

for x1, y1, x2, y2 in queries:
    cx1 = bisect.bisect_left(x_vals, x1)
    cx2 = bisect.bisect_right(x_vals, x2)
    cy1 = bisect.bisect_left(y_vals, y1)
    cy2 = bisect.bisect_right(y_vals, y2)
    
    ans = grid[cx2][cy2] - grid[cx1][cy2] - grid[cx2][cy1] + grid[cx1][cy1]
    print(ans)
import bisect

n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

points.sort()

for a, b in queries:
    count = bisect.bisect_right(points, b) - bisect.bisect_left(points, a)
    print(count)
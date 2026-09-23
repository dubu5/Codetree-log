import heapq

n, m, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

pq = []
for i in range(min(n, k)):
    heapq.heappush(pq, (arr1[i] + arr2[0], i, 0))

for _ in range(k - 1):
    _, i, j = heapq.heappop(pq)
    if j + 1 < m:
        heapq.heappush(pq, (arr1[i] + arr2[j + 1], i, j + 1))

print(pq[0][0])
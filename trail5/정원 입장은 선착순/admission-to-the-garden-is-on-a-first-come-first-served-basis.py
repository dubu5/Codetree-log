import sys
import heapq

input = sys.stdin.readline

N = int(input())
a, t = [], []
for _ in range(N):
    ai, ti = map(int, input().split())
    a.append(ai)
    t.append(ti)

people = [(a[i], i, t[i]) for i in range(N)]
people.sort()

pq = []
curr_time = 0
max_wait = 0
idx = 0

while idx < N or pq:
    if not pq and curr_time < people[idx][0]:
        curr_time = people[idx][0]
    
    while idx < N and people[idx][0] <= curr_time:
        heapq.heappush(pq, (people[idx][1], people[idx][0], people[idx][2]))
        idx += 1
        
    if pq:
        orig_idx, arr_time, duration = heapq.heappop(pq)
        max_wait = max(max_wait, curr_time - arr_time)
        curr_time += duration

print(max_wait)
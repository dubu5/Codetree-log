import heapq
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    
    left_heap = []
    right_heap = []
    medians = []
    
    for i in range(m):
        val = arr[i]
        
        if not left_heap or val <= -left_heap[0]:
            heapq.heappush(left_heap, -val)
        else:
            heapq.heappush(right_heap, val)
            
        if len(left_heap) > len(right_heap) + 1:
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
        elif len(right_heap) > len(left_heap):
            heapq.heappush(left_heap, -heapq.heappop(right_heap))
            
        if i % 2 == 0:
            medians.append(-left_heap[0])
            
    print(*medians)
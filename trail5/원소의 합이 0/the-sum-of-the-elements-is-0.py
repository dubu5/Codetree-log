n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Please write your code here.
ab_sum = {}
for a in A:
    for b in B:
        s = a + b
        if s in ab_sum:
            ab_sum[s] += 1
        else:
            ab_sum[s] = 1

count = 0
for c in C:
    for d in D:
        target = -(c + d)
        if target in ab_sum:
            count += ab_sum[target]

print(count)
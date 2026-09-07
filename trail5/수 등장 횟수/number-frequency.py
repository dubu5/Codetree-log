from collections import Counter

n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
count = {}
for x in arr:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

result = []
for x in nums:
    if x in count:
        result.append(str(count[x]))
    else:
        result.append("0")

print(" ".join(result))
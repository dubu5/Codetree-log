n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
count = {}
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

print(max(count.values()))
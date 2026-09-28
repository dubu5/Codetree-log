n, k = map(int, input().split())
arr = list(map(int, input().split()))

current_sum = sum(arr[:k])
max_sum = current_sum

for i in range(k, n):
    current_sum = current_sum - arr[i - k] + arr[i]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
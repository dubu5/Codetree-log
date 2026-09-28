n = int(input())
arr = list(map(int, input().split()))

total_sum = sum(arr)

if total_sum % 4 != 0:
    print(0)
else:
    target = total_sum // 4
    cnt1 = 0
    cnt2 = 0
    ans = 0
    curr_sum = 0
    
    for i in range(n - 1):
        curr_sum += arr[i]
        
        if curr_sum == 3 * target:
            ans += cnt2
        if curr_sum == 2 * target:
            cnt2 += cnt1
        if curr_sum == target:
            cnt1 += 1
            
    print(ans)
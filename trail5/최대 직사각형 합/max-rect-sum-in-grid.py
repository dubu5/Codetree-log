n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_sum = float('-inf')

for i in range(n):
    temp = [0] * n
    for j in range(i, n):
        current_max = float('-inf')
        global_max = float('-inf')
        
        for k in range(n):
            temp[k] += arr[j][k]
            
            if current_max > 0:
                current_max += temp[k]
            else:
                current_max = temp[k]
                
            if current_max > global_max:
                global_max = current_max
                
        if global_max > max_sum:
            max_sum = global_max

print(max_sum)
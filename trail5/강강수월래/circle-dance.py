N, M, Q = map(int, input().split())

circle_size = []
student_nums = []

for _ in range(M):
    nums = list(map(int, input().split()))
    circle_size.append(nums[0])
    student_nums.append(nums[1:])

command = []
A = []
B = []

for _ in range(Q):
    query = list(map(int, input().split()))
    command.append(query[0])
    A.append(query[1])
    if query[0] in [1, 2]:
        B.append(query[2])
    else:
        B.append(0)

prev_node = {}
next_node = {}

for i in range(M):
    circle = student_nums[i]
    sz = circle_size[i]
    for j in range(sz):
        curr = circle[j]
        nxt = circle[(j + 1) % sz]
        prv = circle[(j - 1) % sz] 
        
        next_node[curr] = nxt
        prev_node[curr] = prv

for i in range(Q):
    cmd = command[i]
    a = A[i]
    
    if cmd == 1:
        b = B[i]
        next_a = next_node[a]
        prev_b = prev_node[b]
        
        next_node[a] = b
        prev_node[b] = a
        
        next_node[prev_b] = next_a
        prev_node[next_a] = prev_b
        
    elif cmd == 2:
        b = B[i]
        prev_a = prev_node[a]
        prev_b = prev_node[b]
        
        next_node[prev_b] = a
        prev_node[a] = prev_b
        
        next_node[prev_a] = b
        prev_node[b] = prev_a
        
    elif cmd == 3:
        min_student = a
        curr = next_node[a]
        while curr != a:
            if curr < min_student:
                min_student = curr
            curr = next_node[curr]
            
        result = []
        curr = min_student
        while True:
            result.append(curr)
            curr = prev_node[curr]
            if curr == min_student:
                break
                
        print(*result)
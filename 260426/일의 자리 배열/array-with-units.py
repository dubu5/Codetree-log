A = list(map(int, input().split()))

for i in range(10):
    if i<=1:
        print(A[i], end=' ')
    else:
        A.append((A[i-2] + A[i-1]) % 10)
        print(A[i], end=' ')
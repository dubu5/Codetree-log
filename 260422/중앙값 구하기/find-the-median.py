A, B, C = map(int, input().split())

if A>B:
    if A<C:
        print(A)
    elif B>C:
        print(B)
    else:
        print(C)
else:
    if B<C:
        print(B)
    elif A>C:
        print(A)
    else:
        print(C)
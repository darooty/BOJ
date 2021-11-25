N, A, B = map(int, input().split())
for i in range((N + 1) // 2):
    if abs(A - B) == 1:
        if (A % 2 == 0 and B < A) or (B % 2 == 0 and A < B):
            print(i + 1)
            break
    A = (A + 1) // 2
    B = (B + 1) // 2 

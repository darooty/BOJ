N = int(input())
ans = 0
for i in range(1, N + 1):
    check = True
    for idx, j in enumerate(list(map(int, str(i)))):
        if idx == 0:
            prv = j
        elif idx == 1:
            diff = prv - j
            prv = j
        elif diff == prv - j:
            prv = j
        else:
            check = False
            break
    if check:
        ans += 1
print(ans)
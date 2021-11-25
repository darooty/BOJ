def go(start, cnt, rlt):
    global ans
    if len(rlt) and sum(rlt) == S:
        ans += 1
    if cnt == N:
        return
    for i in range(start, N):
        rlt.append(Nums[i])
        go(i + 1, cnt + 1, rlt)
        rlt.pop()

N, S = map(int, input().split())
Nums = list(map(int, input().split()))
ans = 0
go(0, 0, [])
print(ans)
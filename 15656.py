def go(cnt, rlt):
    if cnt == M:
        print(*rlt)
        return
    for i in range(N):
        rlt.append(Nums[i])
        go(cnt + 1, rlt)
        rlt.pop()


N, M = map(int, input().split())
Nums = sorted(list(map(int, input().split())))
go(0, [])
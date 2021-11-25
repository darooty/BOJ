def go(cnt, rlt):
    prv = -1
    if cnt == M:
        print(*rlt)
        return
    for i in range(N):
        if prv != Nums[i]:
            rlt.append(Nums[i])
            go(cnt + 1, rlt)
            prv = Nums[i]
            rlt.pop()

N, M = map(int, input().split())
Nums = sorted(list(map(int, input().split())))
go(0, [])
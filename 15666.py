def go(start, cnt, rlt):
    prv = -1
    if cnt == M:
        print(*rlt)
        return
    for i in range(start, N):
        if prv != Nums[i]:
            rlt.append(Nums[i])
            go(i, cnt + 1, rlt)
            prv = Nums[i]
            rlt.pop()

N, M = map(int, input().split())
Nums = sorted(list(map(int, input().split())))
go(0, 0, [])
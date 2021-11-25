def go(start, cnt, rlt):
    prv = -1
    if cnt == M:
        print(*rlt)
    for i in range(start, N):
        if prv != Nums[i]:
            rlt.append(Nums[i])
            go(i + 1, cnt + 1, rlt)
            rlt.pop()
            prv = Nums[i]

N, M = map(int, input().split())
Nums = sorted(list(map(int, input().split())))
go(0, 0, [])
def go(cnt, rlt):
    prv = None
    if cnt == M:
        print(*rlt)
        return
    for i in range(N):
        if not V[i] and prv != Nums[i]:
            V[i] = 1
            rlt.append(Nums[i])
            go(cnt + 1, rlt)
            prv = Nums[i]
            V[i] = 0
            rlt.pop()

N, M = map(int, input().split())
Nums = sorted(list(map(int, input().split())))
V = [0] * N
go(0, [])
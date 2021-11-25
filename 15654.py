def go(cnt, rlt):
    if cnt == M:
        print(*rlt)
        return
    for i in range(N):
        if not V[i]:
            V[i] = 1
            rlt.append(Nums[i])
            go(cnt + 1, rlt)
            V[i] = 0
            rlt.pop()

N, M = map(int, input().split())
Nums = sorted(list(map(int, input().split())))
V = [0] * N
go(0, [])
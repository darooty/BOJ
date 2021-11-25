def go(start, cnt, rlt):
    if cnt == M:
        print(*rlt)
        return
    for i in range(start, N):
        rlt.append(i + 1)
        go(i, cnt + 1, rlt)
        rlt.pop()

N, M = map(int, input().split())
go(0, 0, [])
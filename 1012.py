def dfs(cur_r, cur_c, grp):
    V[cur_r][cur_c] = grp
    for dx, dy in dr:
        nxt_r, nxt_c = cur_r + dx, cur_c + dy
        if 0 <= nxt_r <= N - 1 and 0 <= nxt_c <= M - 1 and V[nxt_r][nxt_c] != grp:
            dfs(nxt_r, nxt_c, grp)

T = int(input())
M, N, K = map(int, input().split())
V = [[0]*M for _ in range(N)]
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for _ in range(T):
    A = [[0] * M for _ in range(N)]
    for k in range(K):
        a, b = map(int, input().split())
        A[b][a] = 1
    cnt = 0
    for r in range(N):
        for c in range(M):
            if A[r][c] == 1 and V[r][c] != k:
                dfs(r, c, k)
                cnt += 1
    print(cnt)

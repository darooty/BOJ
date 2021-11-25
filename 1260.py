import collections


def dfs(v, grp):
    visit[v - 1] = grp
    print(v, end=' ')
    for i in ad[v - 1]:
        if visit[i] != grp:
            dfs(i + 1, grp)


def bfs(v, grp):
    q = collections.deque()
    q.append(v)
    visit[v - 1] = grp
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in ad[v - 1]:
            if visit[i] != grp:
                visit[i] = grp
                q.append(i + 1)


N, M, V = map(int, input().split())
ad = [list() for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    ad[a - 1].append(b - 1)
    ad[b - 1].append(a - 1)
for i in range(N):
    ad[i] = sorted(ad[i])
visit = [0] * N
dfs(V, 1)
print()
bfs(V, 2)

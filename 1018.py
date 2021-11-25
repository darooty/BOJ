N, M = map(int, input().split())
Board = [list(map(str, input())) for i in range(N)]
WBoard = [['W', 'B']*4, ['B', 'W'] * 4] * 4
BBoard = [['B', 'W'] * 4, ['W', 'B']*4] * 4
ans = 64

for r in range(N - 7):
    for c in range(M - 7):
        wtmp, btmp = 0, 0
        for i in range(8):
            for j in range(8):
                if WBoard[i][j] != Board[r + i][c + j]:
                    wtmp += 1
                if BBoard[i][j] != Board[r + i][c + j]:
                    btmp += 1
        ans = min(ans, wtmp)
        ans = min(ans, btmp)
print(ans)




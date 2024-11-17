N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
rows_to_off = set()
cols_to_off = set()

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            rows_to_off.add(i)
            cols_to_off.add(j)
for i in range(N):
    for j in range(M):
        if i in rows_to_off or j in cols_to_off:
            grid[i][j] = 0
for row in grid:
    print(' '.join(map(str, row)))

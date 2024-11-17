n = int(input())
matrix = []
for _ in range(n):
  row = list(map(int, input().split()))
  matrix.append(row)
for i in range(n):
  for j in range(n // 2):
    matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
for i in range(n):
  print(*matrix[i])

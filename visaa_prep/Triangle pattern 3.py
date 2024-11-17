N = int(input())
for i in range(1, N + 1):
    left_triangle = ''.join(str(j) for j in range(1, i + 1))
    right_triangle = ''.join(str(j) for j in range(i, 0, -1)).rjust(N)
    print(left_triangle.ljust(N) + right_triangle)

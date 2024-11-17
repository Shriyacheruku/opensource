N = int(input())
arr = list(map(int, input().split()))
K = int(input())
K = K % N
rotatedarray = arr[-K:] + arr[:-K]
print(' '.join(map(str, rotatedarray)))

n = int(input())
arr = list(map(int, input().split()))
sorted = True
for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        sorted = False
        break
print("true" if sorted else "false")

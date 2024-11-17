T = int(input())
results = []
for _ in range(T):
    X = int(input())
    if 67 <= X <= 45000:
        results.append("YES")
    else:
        results.append("NO")
for res in results:
    print(res)

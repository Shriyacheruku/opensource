N = int(input())
sticks = list(map(int, input().split()))
sticks.sort(reverse=True)
for i in range(N - 2):
    if sticks[i] < sticks[i + 1] + sticks[i + 2]:
        print(sticks[i] + sticks[i + 1] + sticks[i + 2])
        break
else:
    print(-1)

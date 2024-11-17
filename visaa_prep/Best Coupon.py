x = int(input())
per = x * 0.10
flat_100 = 100
max_dis = max(per, flat_100)
amount = x - max_dis
print(int(amount))

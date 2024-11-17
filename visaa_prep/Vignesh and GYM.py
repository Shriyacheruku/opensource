x, y, z = map(int, input().split())
cost = x
trainer_cost = x+y
if trainer_cost <= z:
    print(2)
elif cost <= z:
    print(1)
else:
    print(0)

def sum_of_digits(n):
  sum = 0
  while n:
    sum += n % 10
    n //= 10
  return sum
n = int(input())
if sum_of_digits(n) % 2 == 0:
  print("Vignesh")
else:
  print("Charan")

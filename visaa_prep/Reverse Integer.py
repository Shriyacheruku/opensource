def reverse_integer(n):
  is_negative = n < 0
  n = abs(n)
  reversed_n = 0
  while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n //= 10
  if reversed_n > 2**31 - 1 or reversed_n < -2**31:
    return 0
  if is_negative:
    reversed_n *= -1
  return reversed_n
n = int(input())
reversed_n = reverse_integer(n)
print(reversed_n)

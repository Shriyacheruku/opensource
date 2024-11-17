def consecutive_absent(days):
  max_absent = 0
  cur_absent = 0
  for day in days:
    if day == 0:
      cur_absent += 1
    else:
      max_absent = max(max_absent, cur_absent)
      cur_absent = 0
  max_absent = max(max_absent, cur_absent)
  return max_absent
if __name__ == "__main__":
  n = int(input())
  days = list(map(int, input().split()))
  max_absent_days = consecutive_absent(days)
  print(max_absent_days)

max_num, max_sum_result = [int(n) for n in input().split()]
count = 0

for left_num in range(1, max_num + 1):
  for right_num in range(1, max_num + 1):
      if left_num + right_num <= max_sum_result:
        count += 1
print(count)

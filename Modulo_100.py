count = int(input())
num_list = [int(n) for n in input().split()]
num_result = 0

for n in num_list:
  num_result += n

print(num_result % 100)

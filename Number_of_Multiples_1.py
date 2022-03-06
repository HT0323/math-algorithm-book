max_num, element_1, element_2 = [int(n) for n in input().split()]

count = 0
for i in range(1, max_num + 1):
	if i % element_1 == 0 or i % element_2 == 0:
		count += 1

print(count)

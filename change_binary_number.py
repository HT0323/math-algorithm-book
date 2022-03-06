result = ""

while(input > 0):
  result = "1" + result if input() % 2 == 1 else "0" + result
  input = int(input /  2)

print(result)

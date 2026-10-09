#print the sum of all digits

number = 321

total = 0

while number>0:
  x = number % 10
  total += x
  number = number//10

print(total)

n = int(input("enter odd no: "))
num = n // 2

for i in range(n):
  for j in range(n):
      if i == num or j == num:
          print("*", end=" ")
      else:
          print(" ", end=" ")
  print()

# Enter odd size: 5
#     *     
#     *     
# * * * * * 
#     *     
#     *  
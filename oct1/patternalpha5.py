n = int(input("Enter odd size: "))
center = n // 2

for i in range(n):
  for j in range(n):
      if i == center or j == center:
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
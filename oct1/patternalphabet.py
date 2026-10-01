n = int(input("enter number of rows:"))

for i in range (n):
  for j in range (i):
    print(chr(65+j), end=" ")
  print()



# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
# A B C D E F 
# A B C D E F G 
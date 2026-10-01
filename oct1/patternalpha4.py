n = int(input("     add:"))

for i in range (n):
  print(' '*(n-i+1), end=" ")
  for j in range (2*i+1):
    if ( j==0 or j==2*i or i==n-1):
      print(chr(65+j), end=" ")
    else:
      print(" ", end=" ")

  print()

  #    add:4
  #     A 
  #    A   C 
  #   A       E 
  #  A B C D E F G 
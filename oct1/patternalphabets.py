n = int(input("enter number of rows:"))
num=0
for i in range (n):
  for j in range (i):
    print(chr(65+num), end=" ")
    num = num+1
  print()


# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
# P Q R S T U 
# V W X Y Z [ \ 
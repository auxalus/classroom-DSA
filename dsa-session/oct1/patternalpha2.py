n = int(input("enter number of rows:"))

for i in range (n):
  for j in range (i+1):
    print(chr(65+i), end=" ")
  print()


# enter number of rows:8
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
# F F F F F F 
# G G G G G G G 
# H H H H H H H H 
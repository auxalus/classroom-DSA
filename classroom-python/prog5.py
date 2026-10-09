# print pattern

# *
# ##
# ***
# ####

n = int(input("enter number of rows :"))

for i in range(1, n+1):
    if i % 2 != 0:
        print("*" * i)
    else:
        print("#" * i)
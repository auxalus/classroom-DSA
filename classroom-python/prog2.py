# create a heterogenous list of nums and names. split the list from highest number

this_list = ['one','two',5,'cat',6,8,3]
number = []

for i in this_list:
  if type(i) == int:
    number.append(i)


print(max(number))


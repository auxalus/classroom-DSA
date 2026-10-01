N = int(input("Enter extra number:"))

thisnumbers = [2, 7, 9, 0, 2, 12, 33]
thisnumbers.append(N)

for first_position in range(len(thisnumbers)):
	for second_position in range(first_position + 1, len(thisnumbers)):
		if thisnumbers[first_position] > thisnumbers[second_position]:
			temporary_number = thisnumbers[first_position]
			thisnumbers[first_position] = thisnumbers[second_position]
			thisnumbers[second_position] = temporary_number

print(thisnumbers)
print("smallest number is " , thisnumbers[0])
print("largest number is " , thisnumbers[-1])
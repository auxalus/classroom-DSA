N = int(input("Enter extra number: "))

thisnumbers = [3, 5, 9]
thisnumbers.append(N)

evennumbers = [number for number in thisnumbers if number % 2 == 0]
oddnumbers = [number for number in thisnumbers if number % 2 != 0]


sumofeven = sum(evennumbers)
sumofodd = sum(oddnumbers)

print("Even numbers:", sumofeven)
print("Odd numbers:", sumofodd)
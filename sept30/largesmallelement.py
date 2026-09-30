# WAP to find the maximum, second maximum, minimum, and second minimum.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if len(numbers) < 2:
    print("Please enter at least two numbers.")
else:
    numbers.sort()

    print("Maximum:", numbers[-1])
    print("Second maximum:", numbers[-2])
    print("Minimum:", numbers[0])
    print("Second minimum:", numbers[1])

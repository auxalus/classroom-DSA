# accept the name and check if its palindrome

the_name = input("enter the name : ")

if the_name == the_name[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
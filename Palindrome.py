string = input("Enter a string: ")

reversed_string = string[::-1]

if string.lower() == reversed_string.lower():
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
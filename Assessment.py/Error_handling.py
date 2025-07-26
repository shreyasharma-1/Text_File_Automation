"""
1	
 Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.

2	
 Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.

3	
 Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.

4	
 Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.

"""

# question = 1
try:
    a = int(input())
    b = int(input())
    result = a / b
    print(result)
except Exception as e:
    print("Error:", e)

# question = 2
try:
    num = int(input())
    if num < 2:
        print("Not Prime")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
except ValueError:
    print("Error: Enter a valid number")

# question = 3
try:
    fname = input()
    with open(fname, "r") as file:
        content = file.read()
        print(content.title())
except FileNotFoundError:
    print("Error: File not found")


# question = 4
numbers = [10, -5, 20, -15, 25, -30, 35, -40, 45, -50]
try:
    index = int(input())
    if numbers[index] >= 0:
        print("Positive")
    else:
        print("Negative")
except IndexError:
    print("Error: Invalid index")

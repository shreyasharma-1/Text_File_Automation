"""
 Write a program to check if a given number is Positive, Negative, or Zero.
"""
def check_number(num):
    if num == 0:
        return "Zero"
    elif num > 0:
        return "Positive"
    else:
        return "Negative"
print(check_number(10))   # Output: Positive
print(check_number(-5))   # Output: Negative    
print(check_number(0))    # Output: Zero

"""
Write a program to check if a given number is odd or even.
"""
def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_odd_even(10))  # Output: Even
print(check_odd_even(7))   # Output: Odd

"""
 Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
lastDigit(7, 17) → true                                                
lastDigit(6, 17) → false
lastDigit(3, 113) → true
"""
def last_digit(num1, num2):
    if num1 % 10 == num2 % 10:
        return True
    else:
        return False
    
print(last_digit(7, 17))    # Output: True
print(last_digit(6, 17))    # Output: False 

"""
 Write a program to print numbers from 1 to 10 in a single row with one tab space.
"""
def print_numbers():
    for i in range(1, 11):
        print(i, end='\t')

"""
Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.
"""
def print_even_numbers(start, end):
    for num in range(23, 58):
        if num % 2 == 0:
            print(num)  

"""
 Write a program to check if a given number is prime or not.
"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

"""
 Write a program to print prime numbers between 10 and 99.
"""
def print_prime_numbers(start, end):
    for num in range(10,100):
        if is_prime(num):
            print(num)

"""
Write a program to print the sum of all the digits of a given number.
Example:
I/P:1234
O/P:10
"""
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

"""
Write a program to reverse a given number and print.

Example:1
I/P: 1234
O/P:4321

Example:2
I/P:1004
O/P:4001
"""
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return reversed_num

"""
Write a program to find if the given number is palindrome or not

Example:1
I/P:110011
O/P: 110011 is a palindrome.

Example:2
I/P:1234
O/P: 1234 is not a palindrome.
"""
def is_palindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    if original_num == reversed_num:
        return "palindrome."
    else:
        return "not a palindrome."
    

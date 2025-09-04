"""Q1)Write a function to return the sum of all numbers in a list.
Sample List (8, 2, 3, 0, 7)
Expected Output: 20"""

def sum_of_list(numbers):
    return sum(numbers)

sample_list = [8, 2, 3, 0, 7]
print("Sum:", sum_of_list(sample_list)) 


"""Q2)Write a function to return the reverse of a string.
Sample String: "1234abcd"
Expected Output: "dcba4321"  """

def reverse_string(s):
    return s[::-1]

sample_string = "1234abcd"
print("Reversed:", reverse_string(sample_string)) 

"""Q3)Write a function to calculate and return the factorial of a
number (a non-negative integer)."""

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print("Factorial:", factorial_recursive(5))  


"""Q4)Write a function that accepts a string and prints the number
of upper case letters and lower case letters in it."""

def count_case_letters(s):
    upper_count = 0
    lower_count = 0

    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("No. of Upper case characters:", upper_count)
    print("No. of Lower case characters:", lower_count)

sample_string = "Hello World!"
count_case_letters(sample_string)


"""Q5)Write a function to print the even numbers from a given list.
List is passed to the function as an argument.
Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Result: [2, 4, 6, 8] """

def print_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", even_numbers)

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_numbers(sample_list)


"""Q6)Write a function that takes a number as a parameter and checks
whether the number is prime or not."""

def is_prime(n):
    if n <= 1:
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

number = 13
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

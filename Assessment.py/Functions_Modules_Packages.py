#Functions

"""
1	
 Write a function to return the sum of all numbers in a list.  
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
	
2	
 Write a function to return the reverse of a string.  
Sample String : "1234abcd"
Expected Output : "dcba4321"

3	
 Write a function to calculate and return the factorial of a number (a non-negative integer).

4	
 Write a function that accepts a string and prints the number of upper case letters and lower case letters in it. 
	
5	
 Write a function to print the even numbers from a given list. List is passed to the function as an argument. 
 Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
	
6	
 Write a function that takes a number as a parameter and checks whether the number is prime or not.

"""

# question = 1
def sum_list(numbers):
    return sum(numbers)

print(sum_list([8, 2, 3, 0, 7]))

# question = 2
def reverse_string(s):
    return s[::-1]

print(reverse_string("1234abcd"))

# question = 3
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(5))

# question = 4
def count_Case(s):
    upper = 0
    lower = 0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    print(upper)
    print(lower)

count_Case("Hello World")

# question = 5
def even(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    print(evens)

even([1, 2, 3, 4, 5, 6, 7, 8, 9])


# question = 6
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(prime(7))


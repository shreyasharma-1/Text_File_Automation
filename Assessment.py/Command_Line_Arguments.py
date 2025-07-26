"""
1	
 Write a program to accept two numbers as command line arguments and display their sum.

2	
 Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

3	
 Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

"""

# question = 1
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
print(a + b)

# question = 2
import sys
print("File Name:", sys.argv[0])
print("Welcome Message:", sys.argv[1])

# question = 3
import sys
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

nums = list(map(int, sys.argv[1:]))
total = 0
for n in nums:
    if is_prime(n):
        total += n
print(total)



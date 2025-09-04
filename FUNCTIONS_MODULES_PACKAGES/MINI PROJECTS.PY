"""PROJECT1:- Write a Python function that accepts a hyphen-separated
sequence of colors as input and returns the colors in a hyphen-
separated sequence after sorting them alphabetically.

Constraint: All the colors will be completely in either lower case
or upper case.

Sample input 1: green-red-yellow-black-white
Sample output 1: black-green-red-white-yellow
Sample input 2: PINK-BLUE-TAN-PURPLE
Sample output 2: BLUE-PINK-PURPLE-TAN"""

def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    colors.sort()
    return '-'.join(colors)

print(sort_colors("green-red-yellow-black-white"))
print(sort_colors("PINK-BLUE-TAN-PURPLE"))       

"""PROJECT2:- Create a Python module with the following functions:
Function Name1 - ispalindrome(name)
Task - Given the user name as input, this function should tell us
whether the name is a palindrome or not.

Function Name2 - count_the_vowels(name)
Task - Given the user name as input, this function should tell us
how many vowels are present in it.

Function Name3 - frequency_of_letters(name)
Task - Given the user name as input, this function should tell us
how many times each letter appears in the name.

Note: name will be completely in either lower case or upper case.
Import the module in another python script and test the functions
by passing appropriate inputs.
Sample input 1: bob
Sample output 1: Yes it is a palindrome.
                 No of vowels: 1
                 Frequency of letters: b-2, 0-1 

Sample input 2: marcel bentok tanaka
Sample output 2: No it is not a palindrome.
                 No of vowels: 7
                 Frequency of letters: m-1, a-4, r-1, c-1, e-2, 1-1,
                   b-1, n-2, 1-2, 0-1, k-2 """

import Name_module

name1 = "bob"
print("Input:", name1)
print(Name_module.ispalindrome(name1))
print(Name_module.count_the_vowels(name1))
print(Name_module.frequency_of_letters(name1))
print()

name2 = "marcel bentok tanaka"
print("Input:", name2)
print(Name_module.ispalindrome(name2))
print(Name_module.count_the_vowels(name2))
print(Name_module.frequency_of_letters(name2))




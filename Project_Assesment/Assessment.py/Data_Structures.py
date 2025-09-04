"""
1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
List	

2.  Write a program to append a new item to the end of the list.
List	

3. Write a program to reverse the order of the items in the list.
List	

4. Write a program to print the number of occurrences of a specified element in a list.
List	

5. Write a program to append the items of list1 to list2 in the front.
List	

6. Write a program to insert a new item before the second element in an existing list.
List	
	
7. Write a program to remove the item from a specified index in a list.
List	
	
8. Write a program to remove the first occurrence of a specified element from a list.
"""

# question = 1
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

# question = 2
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

# question = 3
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)

# question = 4
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.count(2))

# question = 5
list1 = [1, 2, 3]
list2 = [4, 5, 6]   
list2 = list1 + list2
print(list2)

# question = 6
items = [100, 200, 300, 400]
items.insert(1, 150)
print(items)

# question = 7
items = [10, 20, 30, 40, 50]
del items[2]
print(items)

# question = 8
items = [5, 3, 7, 3, 9]
items.remove(3)
print(items)


#Dictionary

"""
1		
 Write a program to add a key and value to a dictionary.   
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30} 

2	
 Write a program to concatenate the following dictionaries to create a new one.  
Sample Dictionary : 
dic1={1:10, 2:20}  dic2={3:30, 4:40}  dic3={5:50,6:60} 
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

3	
 Write a program to check if a given key already exists in a dictionary.

4	
 Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.

5
 Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.

6	
 Write a program to sum all the values in a dictionary, considering the values will be of int type.

"""

# question = 1
d = {0: 10, 1: 20}
d[2] = 30
print(d)

# question = 2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
d = {}
d.update(dic1)
d.update(dic2)
d.update(dic3)
print(d)

# question = 3
d = {1: 100, 2: 200, 3: 300}
key = 2
print(key in d)

# question = 4
d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
    print(k)
for v in d.values():
    print(v)
for k, v in d.items():
    print(k, v)

# question = 5
d = {}
for i in range(1, 16):
    d[i] = i * i
print(d)

# question = 6
d = {'x': 100, 'y': 200, 'z': 300}
print(sum(d.values()))


#Tuples

"""
1	
 Write a program to print the 4th element from first and 4th element from last in a tuple.

2	
 Write a program to check whether an element exists in a tuple or not.

3	
 Write a program to convert a list into a tuple.
	
4
 Write a program to find the index of an item in a tuple.

5
 Write a program to replace last value of tuples in a list to 100.  
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

"""
# question = 1
t = (10, 20, 30, 40, 50, 60, 70, 80)
print(t[3])
print(t[-4])

# question = 2
t = (5, 10, 15, 20)
x = 15
print(x in t)

# question = 3
l = [1, 2, 3, 4]
t = tuple(l)
print(t)

# question = 4
t = (10, 20, 30, 40)
print(t.index(30))

# question = 5
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
l = [t[:-1] + (100,) for t in l]
print(l)


#Sets

"""
1	
 Write a program to remove a given item from the set.

2		
 Write a program to create an intersection of sets.

3		
 Write a program to create an union of sets.

4	
 Write a program to find the maximum and minimum value in a set.

"""
# question = 1
s = {10, 20, 30, 40}
s.remove(30)
print(s)

# question = 2
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = s1 & s2
print(s3)

# question = 3
s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = s1 | s2
print(s3)

# question = 4
s = {25, 50, 10, 75, 5}
print(max(s))
print(min(s))


#Strings

"""
1	
 Write a program to count the number of upper and lower case letters in a String.

2		
 Write a program that will check whether a given String is Palindrome or not.

3	
 Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >=2. 
If input is "Wipro" then output should be "WiWiWiWiWi".

4	
 Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".
	
5	
 Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive. For example if the inputs are “Wipro” and 3, then the output should be “propropro”.

"""

# question = 1
s = "Hello World"
upper = 0
lower = 0
for c in s:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1
print(upper)
print(lower)

# question = 2
s = "madam"
print(s == s[::-1])

# question = 3
s = "Wipro"
print(s[:2] * len(s))

# question = 4
s = "xHix"
if s.startswith('x'):
    s = s[1:]
if s.endswith('x'):
    s = s[:-1]
print(s)

# question = 5
s = "Wipro"
n = 3
print(s[-n:] * n)

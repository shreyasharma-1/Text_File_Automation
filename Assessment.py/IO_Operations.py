"""
1	
 Write a program to read the entire content from a txt file and display it to the user.
File Handling	
2	
 Write a program to read first n lines from a txt file. Get n as user input.
	
3	
 Write a program to accept input from user and append it to a txt file.
	
4	
 Write a program to read contents from a txt file line by line and store each line into a list.
	
5	
 Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

6	
 Write a program to count the frequency of a user entered word in a txt file.

"""

# question = 1
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# question = 2
n = int(input())
with open("sample.txt", "r") as file:
    for i in range(n):
        print(file.readline(), end="")


# question = 3
data = input()
with open("sample.txt", "a") as file:
    file.write(data + "\n")

# question = 4
with open("sample.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    print(lines)


# question = 5
with open("sample.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
    print(longest)

# question = 6
word = input()
with open("sample.txt", "r") as file:
    content = file.read()
    count = content.split().count(word)
    print(count)

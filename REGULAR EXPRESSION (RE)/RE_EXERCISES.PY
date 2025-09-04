"""Q1) Write a program to find check if a string has only octal digits. Given 
string ['789', '123', '004"] """

import re
strings = ['789', '123', '004']
for s in strings:
    if re.fullmatch(r'[0-7]+', s):
        print(f"'{s}' is an octal number.")
    else:
        print(f"'{s}' is NOT an octal number.")

"""Q2) Extract the user id, domain name and suffix from the following email addresses.
emails = '''zuck@facebook.com
sunder33@google.com
jeff42@amazon.com'''   """

import re
emails = '''zuck@facebook.com
sunder33@google.com
jeff42@amazon.com'''

pattern = r'(\w+)@(\w+)\.(\w+)'
matches = re.findall(pattern, emails)
for user, domain, suffix in matches:
    print(f"User: {user}, Domain: {domain}, Suffix: {suffix}")

"""Q3) Split the following irregular sentence into proper words
sentence = '''A, very very; irregular sentence''' 
## expected outout: A very very irregular sentence"""

import re
sentence = '''A, very very; irregular sentence'''
cleaned = re.sub(r'[^\w\s]', ' ', sentence)       
cleaned = re.sub(r'\s+', ' ', cleaned).strip()    
print(cleaned)

"""Q4) Clean up the following tweet so that it contains only the user's message. That is,
remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code
today http://t.co/lbwej@px0d cc: @garybernhardt #rstats'''

##desired_output = 'Good advice what I would do differently if I was learning to code today' """

import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code
today http://t.co/lbwej@px0d cc: @garybernhardt #rstats'''

tweet = re.sub(r'http\S+', '', tweet)             
tweet = re.sub(r'RT|cc:', '', tweet)              
tweet = re.sub(r'@[A-Za-z0-9_]+', '', tweet)      
tweet = re.sub(r'#[A-Za-z0-9_]+', '', tweet)     
tweet = re.sub(r'[^\w\s]', '', tweet)             
tweet = re.sub(r'\s+', ' ', tweet).strip()    
print(tweet)

"""Q5) Extract all the text portions between the tags from the following HTML page:
https://raw.githubusercontent.com/selva86/datasets/master/sample.html

Code to retrieve the HTML page is given below:
import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
r.text # html text is contained here

desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header',
'This is a new paragraph!', 'This is a another paragraph!', 'This is a new sentence without a
paragraph break, in bold italics.'] """

import requests
from bs4 import BeautifulSoup

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
soup = BeautifulSoup(r.text, 'html.parser')
output = [text.strip() for text in soup.stripped_strings]
print(output)

"""Q6) Given below list of words, identify the words that begin and end with the same character.
civic
trust
widows
maximum
museums
aa
as  """

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
matching_words = [word for word in words if word[0] == word[-1]]
print(matching_words) 

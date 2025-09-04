# nameutils.py

def ispalindrome(name):
    name = name.replace(" ", "")
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")

def countTheVowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    print(f"No of vowels: {count}")

def frequencyOfLetters(name):
    name = name.replace(" ", "")
    freq = {}
    for char in name:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    freqStr = ", ".join([f"{k}-{v}" for k, v in freq.items()])
    print(f"Frequency of letters: {freqStr}")

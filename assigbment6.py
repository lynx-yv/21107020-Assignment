#Q1
print("\n Write a Python function to check whether a number is perfect or not.")
def perfect(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum += i
    if sum == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")

a = int(input("Enter the number: "))
perfect(a)
print("\n")


# Q2
print('''\n Write a Python function that checks whether a passed string is palindrome or not. Note:
A palindrome is a word, phrase, or sequence that reads the same backward as forward,
e.g., madam or nurses run.''')
print("\n")
string = input("Enter the string: ")
string = string.lower()
def checkPalindrome():
    string2 = string.replace(" " , "")
    rev_string = string2[::-1]
    if rev_string == string2:
        print(f"{string} is a palindrome.")
    else:
        print(f"{string} is not a palindrome")

checkPalindrome()
print("\n")


# Q5
print('''\n Write a Python function that accepts a hyphen-separated sequence of words as input
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow''')


string = input("Enter the hyphen seperated string: ")
def hyphenString():
    list = string.split("-")
    list.sort()
    print("-".join(list))

    
hyphenString()
print("\n")


# Q6
print('''\n Write a Python function to check whether a string is a pangram or not. Note: Pangrams
are words or sentences containing every letter of the alphabet at least once. For
example: \"The quick brown fox jumps over the lazy dog\"''')

string = input("Enter the string to check for a pangram: ")
string.lower()
def checkPangram():
    for i in range(1,27):
        c = chr(64+i)
        c = c.lower()
        
        index = string.find(c)
        if index == -1:
            print("It is not a pangram.")
            a = 0
            break
        else:
            a = 1
            
    if a == 1:
        print("It is a pangram")


checkPangram()
print("\n")

# Q3
print("\n Write a Python function that prints out the first n rows of Pascal's triangle.")
n = int(input("Enter thenumber of rows in pascal triangle: "))
for i in range(n):
    print(11**i)

Password Checker

A simple Python project that checks password strength and suggests a stronger password

Features
Checks if the password is at least 8 characters long
Checks for uppercase letters
Checks for lowercase letters
Checks for numbers
Checks for special characters
Detects spaces in passwords
Gives a password strength score
Suggests a stronger password if some requirements are missing
Keeps the original password character order when creating a suggestion

How It Works

The program checks the password for five different requirements:

Length
Uppercase letter
Lowercase letter
Number
Special character

Each requirement gives 1 point

4–5 points: Strong
2–3 points: Medium
0–1 points: Weak

If the password is missing any requirements, the program creates a suggested password by adding the missing character types

Python
random module
Functions
Loops
Lists
String methods

How to Run
Make sure Python is installed, then run:
python password.py
Enter your password when the program asks for it

I practiced these topics while making this project:
Functions and nested functions
if / elif / else
for and while loops
Lists and pop()
random.choice()
String methods such as isupper(), islower(), isdigit() and isalnum()
Returning values from functions
Working with different data types

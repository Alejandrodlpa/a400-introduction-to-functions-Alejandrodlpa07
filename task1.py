"""
Create a program with 3 function definitions:
function A prints the message "Hello"
function B prints the message "How are you"
function C prints the message "Hi"

Ask the user to enter a letter from A to C
Execute the function of the letter they use.
"""
import task12
from task12 import *

x=input("Enter a letter (A,B or C): ")
if x=="A":
    task12.A()
elif x=="B":
    task12.B()
elif x=="C":
    task12.C()
else:
    print("invalid input")

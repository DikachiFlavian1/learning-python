#calculator.py
# variables int,float,round
#x = int(input("what's x? "))
#y = int(input("what's y? "))
#z = x+y
#print (z)

#floats are used for decimal numbers while round are used to round up a number 

#x = int(input("what's X? "))
#y = int(input("what's Y? "))

#if x > y:
# print("x isgreater than y ")
#elif  x < y:
   # print("x is less than y ")
#else:
 # print("x is equal to y")

 #using loops: loops are used to to repeat a command repeatatively.
#z = 4
#while z !=0:
 #   print("meow")
 #   z = z-1

#list  list is a datatype that repeats a given specified insturction throuh
 #manually inputed functions or python functions for example

#for i in range(10):
 #   print("I'm exhausted")

#for i in (0,1,2): 
#        print ("tell me your name ")

#using using "while true" , "break" ,in a code : when we use whie true code , we are trying to inform the program to 
#run if a statement is true . "the Break" statement instructs the code to stop if the information is true eg
"""
 while True:
    n = int(input("give me  your Mat/num "))
    if n > 0:
        break
for _ in range(n):
         print("I must succed")
         #range is used to list a certain or specific amount of times a code should run after meetin up  criteria
         """

#len the lens just as rane is used to return a  value in a given varioable provided the criterias are met
#for example
"""
students = ("Hermione", "Harry", "Ron" , "james")
for i in range(len(students)):
    print (i,students[i])
    """
   
"""notice we started of by naming a variable "students" and then proceded to asssign names of students to that 
    variable, to print this statement so that each students name runs and the followed by the next student ,
    till our last students , thats when we introduce another variable "i" , the "range" tells it to print the number of
   students  name in the given variable e.g (we have 4 students name ) and then the "lens" tells it to print
   the given characters in the variables.
   the print statement is just to remind it that it is printing the variable "students" in the steps assign to 
   variable "i" hence "print(i,students[i])"
"""

#python dictionaries "making use of curly braces as dictonary "
"""
when we want to implement our dictionarie in python , say to contain a list of  names and department 
an dtrhen print them out to display the given names in the dictionaries , eg 
"""
"""
students = {
   "Johnson": "Blue house",
   "Daniel": "Orange house ",
   "Christable": "White house",
   "Justine": "Green House" 
}

for names in students:
    print(names,students[names],sep=", ")
 """

#note we use square bracket [] when we want to make a list and also,suppose in that list, want to make a data 
# make numerous data dictionary, we achieve this by using curly braces in the square bracket , with each 
# curly braces identifying the give data name or column with its  rowname

 # for  example
"""
students = [ 
    {"Name": "Johnson", "House": "Blue House","Pronouns": "Giant" },
    {"Name": "Daniel", "House": "Orange House","Pronouns": "Lion" }, 
     {"Name": "Christable", "House": "White House","Pronouns": "Goat" },
      {"Name": "Justine", "House": "Green House","Pronouns": "None" }
  ]
for student in students:
     print(student["Name"], student["House"], sep=", ")"""


"""def main():
    game(4)

def game(h eigh):
      for name in range(heigh):
         print("Good News")
main()

def main():
  print_square(4)
def print_square(size):
 for i in range(size):
    for j in range(size):
        print("good", end ="")
    print()
main()


def camel_to_snake(camel_str):
    snake_str = ""
    for char in camel_str:
        if char.isupper():
            snake_str += "_" + char.lower()
        else:
            snake_str += char
    return snake_str

def main():
    camel_case_var = input("Enter a variable name in camel case: ")
    snake_case_var = camel_to_snake(camel_case_var)
    print("Snake case variable name:", snake_case_var)

if __name__ == "__main__":
    main()


def camelcase():
    first_name = input("whats your Name? ")
    prefered_name = input("whats your prefered name? ") 
    print("welcome", first_name,prefered_name) 
camelcase()"""

import sys
if len(sys.argv)<3:
    sys.exit("two few arguement ")

for arg in sys.argv[1:]:
    print("hello, my name is",arg)
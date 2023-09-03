# asking user their name, 
#Name = input("what's your Name? ")
#removinh users excess space input
#Name = Name.strip()
#capitalize users name 
#Name = Name.title()
#print("Hello", Name)
#making the codes shorter 
#name =input("whats your name? ").strip().title()#lerning integers
"""$ python camel.py
camelCase: name
snake_case: Name
$ python camel.py
camelCase:firstName
snake_case:first_name
$ python camel.py
snake_case: prefered_first_name
camel_Case:prefered_First_Name"""
"""def camel_to_snake(camel_str):
    snake_str = ""
    for char in camel_str:
        if char.isupper():
            snake_str += "_" + char.lower()
        else:
            snake_str += char
    return snake_str

def snake_to_camel(snake_str):
    camel_str = ""
    capitalize_next = False
    for char in snake_str:
        if char == "_":
            capitalize_next = True
        else:
            if capitalize_next:
                camel_str += char.upper()
                capitalize_next = False
            else:
                camel_str += char
    return camel_str

def main():
    input_str = input("camelCase: ")
    if "_" in input_str:
        output_str = snake_to_camel(input_str)
        case_type = "camel_Case"
    else:
        output_str = camel_to_snake(input_str)
        case_type = "snake_case"
    
    print(f"{case_type}: {output_str}")

if __name__ == "__main__":
    main()

x = int(input("what's x? "))
print(f"x is {x}" )"""

#using if error condition
#the if error conditions  is triggered when we expect a user to input wrong details instead of the 
# real deatails we need eg.

"""try:
   x = int(input("what's x? "))
except ValueError:
   print("x is not an integer ")
else:
  print(f"x is {x}")"""
   
"""while True:
   try:
    x = int(input("what's x? "))
   except ValueError:
    print("x is not an integer")
   else:
       break
print(f"x is {x}")"""

"""while True:
    try:
        x = int(input("what's x? "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("x is not an integer. Please enter a valid integer.")

print(f"x is {x}")"""

#try , except , else and pass
"""def main():
    height = int(input("Height: ")) 
    pyramid(height)

def pyramid(n):   
     for i in range(n):
          print ("#" *(i+1))

if __name__ == "__main__":        
    main()"""

"""import random
 
names = ["james","denis","Grace","chikwado","Angel"]
random.shuffle(names)
for name in names: 
    print(name) """

#def  names():
 #    given = input("whats your name? ")
#def  given(Name):
 #  for name  in len(Name):
 #   print("hello",name ,"how do you do? ")
#names()
"""
def greet(name):
    print("Hello", name, "how do you do?")

def names():
    given_name = input("What's your name? ")
    greet(given_name)

names()"""
"""import time
def count(end,start =0):
    for x  in range(start,end +1 ):
      print(x)
      time.sleep(1)
    print("done")
count(20,10)"""
#for x in range(2):
#   for y in range(0,15):
 #      print(y,end=" ")
 #  print()

"""def is_alpha(input_string):
     return input_string.isalpha()
def is_alphanumeric(input_string):
     return input_string.isalnum() 

while True: 
     name = input("whats your Name ")
     if is_alpha(name):
          break
     else:
          print("please give us your name in alphabeticle order")
while True:
    mat_num = input("whats your mat/num ")
    if is_alphanumeric(mat_num):
         break
    else:
         print("give us an alphanumerical number")

print(f"your name is  {name} and your mat/num is {mat_num}")"""

"""import sys


for arg in sys.argv:

   print(arg)"""

import sys
if len(sys.argv)<2:
    sys.exit("two few arguement ")

for arg in sys.argv[1:]:
    print("hello, my name is",arg)

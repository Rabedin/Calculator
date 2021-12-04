#!/usr/bin/env python3
#
# Here I'm going to try to create a basic calculator and progressively iterate on it to make it more and more powerful

# Solves an equation using two user defined variables and a user defined operator
#VarA = input("Select your first number:")
#VarB = input("Select your second number:")

# Solves a user defined arithmetic math problem

# Asks the user to input the problem
Operation = input("Enter your operation of choice:")
array = list(Operation)

# arraypos variable initial definition
arraypos = 0
# Debug for len(array)
print(len(array))
# While loop to increment array number
while arraypos < len(array):
   # This if loop will find numbers in the user input and append them to the current working variable
   if arraypos == 0:
       workvariable = array[arraypos]
       arraypos = arraypos + 1
   elif "9" >= array[arraypos] >= "0":
       if workvariable in locals():
          # Next line concatenates the current array item to the working variable
          workvariable = workvariable + array[arraypos]
          arraypos = arraypos + 1
          print(f"work variable is {workvariable}")
       else:
          workvariable = array[arraypos]
          arraypos = arraypos + 1
          print(f"work variable is {workvariable}")
   elif array[arraypos] == ".":
       workvariable = workvariable + array[arraypos]
       arraypos = arraypos + 1
   else:
       if 'var1' in locals():
          if 'var2' in locals():
             print(f"variable 2 is {var2}")
          else:
             var2 = workvariable
             op2 = array[arraypos]
             del workvariable
             arraypos = arraypos + 1
             print(f"variable 2 set to {var2}")
             print(f"operator 2 set to {op2}")
       else:
          var1 = workvariable
          op1 = array[arraypos]
          del workvariable
          arraypos = arraypos + 1
          print(f"variable 1 set to {var1}")
          print(f"operator 1 set to {op1}")

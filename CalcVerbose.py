#!/usr/bin/env python3
#
# Here I'm going to try to create a basic calculator and progressively iterate on it to make it more and more powerful

# Solves a user defined arithmetic math problem

# Asks the user to input the problem
Operation = input("Enter your operation of choice:")

# Slices operation into an array with each digit and operation separate and in order
eqarray = list(Operation)

# variable initial definition
arraypos = 0
workvariable = ""
var1 = ""
var2 = ""

# Debug for len(eqarray)
# print(f"array length is:{len(eqarray)}")

# While loop will go through each part of eqarray, creating the necessary variables
while arraypos < len(eqarray):
   # This if loop will find numbers in the user input and append them to the current working variable
   if arraypos == 0:
       workvariable = eqarray[arraypos]
       arraypos = arraypos + 1
      #  print(f"work variable is {workvariable}")
   elif "9" >= eqarray[arraypos] >= "0":
          workvariable = workvariable + eqarray[arraypos]
          arraypos = arraypos + 1
         #  print(f"work variable is {workvariable}")
   elif eqarray[arraypos] == ".":
       workvariable = workvariable + eqarray[arraypos]
       arraypos = arraypos + 1
   else:
       if var1 !="":
          if var2 !="":
             print(f"variable 2 is {var2}")
          else:
             var2 = workvariable
             op2 = eqarray[arraypos]
             workvariable = ""
             arraypos = arraypos + 1
            #  print(f"variable 2 set to {var2}")
            #  print(f"operator 2 set to {op2}")
       else:
          var1 = float(workvariable)
          op1 = eqarray[arraypos]
          workvariable = ""
          arraypos = arraypos + 1
         #  print(f"variable 1 set to {var1}")
         #  print(f"operator 1 set to {op1}")
else:
   var2 = float(workvariable)

# Defining dictionary with all possible operations
opdict = {
   "+": lambda var1, var2: var1 + var2,
   "-": lambda var1, var2: var1 - var2,
   "*": lambda var1, var2: var1 * var2,
   "/": lambda var1, var2: var1 / var2,
   "%": lambda var1, var2: var1 % var2
}

# Printing original equation followed by solution
if op1 in opdict:
   print(f"{Operation} = {opdict[op1](var1, var2)}")

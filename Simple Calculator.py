# Import of libraries
from termcolor import colored

# Display of options
def Display():
  print(colored("\nOptions:\n--------\n0: Exit\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division", "blue"))
  Input()

# Input of option
def Input():
  global Option
  Option = input(colored("\nOption: ", "blue"))
  Options()

# Sorting of options
def Options():
  if Option == "0":
    Exit()
  elif Option == "1":
    Addition()
  elif Option == "2":
    Subtraction()
  elif Option == "3":
    Multiplication()
  elif Option == "4":
    Division()
  else:
    print(colored("\nInvalid input.", "red"))

# Exit
def Exit():
  print(colored("\nScript exiting...", "red"))
  exit()

# Addition
def Addition():
  try:
    print(colored("\nAddition:\n---------", "blue"))
    First_number = float(input(colored("\nFirst number: ", "blue")))
    Second_number = float(input(colored("\nSecond number: ", "blue")))
    Total = First_number + Second_number
    print(colored(f"\nResult: {Total}", "red"))
    Options()
  except ValueError:
    print(colored("\nInvalid input.", "red"))
    Addition()

# Subtraction
def Subtraction():
  try:
    print(colored("\nSubtraction:\n------------", "blue"))
    First_number = float(input(colored("\nFirst number: ", "blue")))
    Second_number = float(input(colored("\nSecond number: ", "blue")))
    Total = First_number - Second_number
    print(colored(f"\nResult: {Total}", "red"))
    Options()
  except ValueError:
    print(colored("\nInvalid input.", "red"))
    Subtraction()

# Multiplication
def Multiplication():
  try:
    print(colored("\nMultiplication:\n------------", "blue"))
    First_number = float(input(colored("\nFirst number: ", "blue")))
    Second_number = float(input(colored("\nSecond number: ", "blue")))
    Total = First_number * Second_number
    print(colored(f"\nResult: {Total}", "red"))
    Options()
  except ValueError:
    print(colored("\nInvalid input.", "red"))
    Multiplication()

# Division
def Division():
  try:
    print(colored("\nDivision:\n---------", "blue"))
    First_number = float(input(colored("\nFirst number: ", "blue")))
    Second_number = float(input(colored("\nSecond number: ", "blue")))
    Total = First_number / Second_number
    print(colored(f"\nResult: {Total}", "red"))
    Options()
  except ValueError:
    print(colored("\nInvalid input.", "red"))
    Division()
  except ZeroDivisionError:
    print(colored("\nUnable to divide by 0.", "red"))
    Division()

Display()

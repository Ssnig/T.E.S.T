import numpy as np
import tkinter as tk

def arraymaker(arr_num=None):
    if arr_num is None:
        arr_num = []

    num = input("Enter a number: ")

    if num.isdigit():
        num = int(num)
        arr_num.append(num)

        yn = input("Do you want to enter another number? (y/n): ")

        match yn:
            case "y":
                return arraymaker(arr_num)
            case "n":
                print("Exiting the program.")
                print(arr_num)
                return arr_num
    else:
        print("Invalid input. Please enter a valid number.")
        return arraymaker(arr_num)

def twod_arrarymaker():
   row_num = input("Enter the number of rows: ")
   col_num = input("Enter the number of columns: ")
   if row_num.isdigit() and col_num.isdigit():
      row_num = int(row_num)
      col_num = int(col_num)
   else:
      print("Invalid input. Please enter valid numbers for rows and columns.")
      return twod_arrarymaker()
   
   data = []
   for i in range(row_num):
      row = []
      for j in range(col_num):
         num=int(input(f"Enter a number for row {i}, column {j}: "))
         row.append(num)
      data.append(row)
   arr_2d = np.array(data)
   print("Here is the 2D array you created:")
   print(arr_2d)
   return

def two_digit_calculator():
    input_num = str(input("Enter aformula with two numbers and an operator (e.g., 3 + 4): "))
    first_num = None
    operator = None
    second_num = None
    for i in range (len(input_num)):
        if input_num[i] .isdigit():
            if first_num is None:
                first_num = int(input_num[i])
            else:
                second_num = int(input_num[i])
        elif input_num[i] in ['+', '-', '*', '/']:
            operator = input_num[i]
        elif input_num[i] == ' ':
            continue
    if first_num is not None and operator is not None and second_num is not None:
        if operator == '+':
            result = first_num + second_num
        elif operator == '-':
            result = first_num - second_num
        elif operator == '*':
            result = first_num * second_num
        elif operator == '/':
            if second_num != 0:
                result = first_num / second_num
            else:
                print("Error: Division by zero is not allowed.")
                return
        print(f"The result of {first_num} {operator} {second_num} is: {result}")
    else:
        print("Invalid input. Please enter a valid formula.")
        return  
    return 

def start():
    print("Welcome to the number test program!")
    while True:
        print("\nPlease choose an option:")
        print("1. Create a 1D array")
        print("2. Create a 2D array")
        print("3. Use the two-digit calculator")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        match choice:
            case "1":
                arraymaker()
            case "2":
                twod_arrarymaker()
            case "3":
                two_digit_calculator()
            case "4":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 4.")

start()
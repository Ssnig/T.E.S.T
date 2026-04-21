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


print("Here are the list of functions to test:")
print("1. arraymaker()")
print("2. twod_arrarymaker()")



choice = input("Enter the number corresponding to the function you want to test: ")

match choice:
    case "1":
        arraymaker()
    case "2":
        twod_arrarymaker()
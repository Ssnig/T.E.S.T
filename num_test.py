
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


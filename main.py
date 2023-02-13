import utils
import random
import csv

def say_hello(name, mode="mon"):
    return f"good {mode} name"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

        # reader = csv.reader(f) # read the variable f as csv file and store it in reader
        # for row in reader:
        #     print(row)

    while True:
        print("select operation you want to perform-1,2,3,4 or 5: ")
        print("1.enter record")
        print("2.search record")
        print("3.delete record")
        print("4.modify record")
        print("5.exit")

        answer = input("enter choice: ")

        if answer == '2':
            utils.get_record()
        elif answer == '3':
            utils.delete_record()
        elif answer == '4':
            utils.modify_record()
        elif answer == '1':
            utils.create_record()
        elif answer == '5':
            break
        else:
            print("invalid choice")


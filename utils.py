import csv


def create_record(n=1):
    while True:
        firstname = input("Enter firstname: ")
        if len(firstname) == 0:
            print('firstname cannot be empty!!')
            continue
        else:
            break
    lastname = input("Enter lastname: ")
    while True:
        phoneno = input("Enter phoneno: ")
        if len(phoneno) == 0:
            print("phone no cannot be empty!!")
            continue
        else:
            break
    while True:
        age = input("Enter age: ")
        if len(age) == 0:
            break
        if age.isnumeric() == True and int(age)<100:
            age = int(age)
            break
        else:
            print("Enter a  valid number which is less than 100")
    city = input("Enter City: ")
    country = input("Enter Country: ")
    with open('records.csv', mode='a', newline='') as f:
        write = csv.writer(f)
        age = age if len(age) > 0 else "null"
        city = city if len(city) > 0 else "null"
        country = "null" if len(country) == 0 else country
        lastname = "null" if len(lastname) == 0 else lastname
        write.writerow([firstname, lastname, phoneno, age, city, country])
    return True


def search_list(lst, item):
    for i in lst:
        if i == item:
            return True
    return False


def get_record():
    search = input("enter the firstname/city/country/phoneno you want to search: ")
    final=[]
    with open('records.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            result = search_list(row, search)
            if result == True:
                final.append(row)
        return final


def case_modify(n, search, new):
    final = []
    with open('records.csv', mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            result = search_list(row, search)
            if result == True:
                row[n] = new
                final.append(row)
            else:
                final.append(row)
    with open('records.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in final:
            writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5]])
    return True

def modify_record():
    while True:
        search = input("enter the firstname/phoneno/age/lastname/city or country of the person you want to modify: ")
        if len(search)>0:
            break
    while True:
        print("what do you want to modify? -1,2,3,4 or 5: ")
        print("1.phone number")
        print("2.age")
        print("3.first name")
        print("4.last name")
        print("5.city")
        print("6.country")
        print("7.exit")
        answer = input("enter choice: ")
        if answer == '7':
            break
        new = input("enter the modification you want to do or enter to exit:  ")
        if len(new) == 0:
            break
        if answer == '1':
            case_modify(2, search, new)
            return True
        if answer == '2':
            case_modify(3, search, new)
            return True
        if answer == '3':
            case_modify(0, search, new)
            return True
        if answer == '4':
            case_modify(1, search, new)
            return True
        if answer == '5':
            case_modify(4, search, new)
            return True
        if answer == '6':
            case_modify(5, search, new)
            return True



def delete_record():
    delete_user = input("enter the user you want to be deleted: ")
    final = []
    result = False
    with open('records.csv', newline='', mode="r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if line[0] == delete_user:
                result = True
                pass
            else:
                final.append(line)
    with open('records.csv', mode="w", newline='') as csvfile:
        write = csv.writer(csvfile)
        for line in final:
            write.writerow([line[0], line[1], line[2]])
    return result


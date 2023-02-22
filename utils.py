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


def read_case_modify(search):
    final = []
    fields = []
    with open('records.csv', mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            result = search_list(row, search)
            if result == True:
                fields.append(row)
            else:
                final.append(row)
        return fields, final


def write_case_modify(result):
    with open('records.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in result:
            writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5]])
    return True


def _modify(response, new,n):
    if len(response[0]) > 1:
        for idx, el in enumerate(response[0]):
            print(f"{idx + 1}. {el}")
        option = input("enter the number of record to edit")
        int_option = int(option)
        response[0][int_option - 1][n] = new
        response[0].extend(response[1])
        write_case_modify(response[0])
    else:
        response[0][0][n] = new
        response[0].extend(response[1])
        write_case_modify(response[0])
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
            response = read_case_modify(search)
            _modify(response, new, 2)
            return True

        if answer == '2':
            response = read_case_modify(search)
            _modify(response, new, 3)
            return True
        if answer == '3':
            response = read_case_modify(search)
            _modify(response, new, 0)
            return True
        if answer == '4':
            response = read_case_modify(search)
            _modify(response, new, 1)
            return True
        if answer == '5':
            response = read_case_modify(search)
            _modify(response, new, 4)
            return True
        if answer == '6':
            response = read_case_modify(search)
            _modify(response, new, 5)
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


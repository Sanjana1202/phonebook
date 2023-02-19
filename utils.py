import csv


def create_record(n=1):
    # todo: allow user to enter only int for age and
    #  add multiple headers like location, photo, country and city.
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


def get_record():
    # todo: allow user to search by address, multiple criteria
    name = input("enter the name you want to search: ")
    with open('records.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == name:
                return row
        return None

def modify_record():
    # todo: ability to modify more than one entries at a time.
    name = input("enter the name of the person you want to modify: ")
    age = input(" enter the new age of the person: ")
    final = []
    with open('records.csv', mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == name:
                row[1] = age
                final.append(row)
            else:
                final.append(row)

    with open('records.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in final:
            writer.writerow([row[0], row[1], row[2]])
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


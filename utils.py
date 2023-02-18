import csv


def create_record(n=1):
    # todo: allow user to enter only int for age and string for name, add multiple headers like location, photo, country and city.
    name = input("enter name: ")
    age = input("enter age: ")

    with open('records.csv', mode='a', newline='') as f:
        write = csv.writer(f)
        write.writerow([name, age])
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


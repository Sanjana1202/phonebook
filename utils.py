d = {}


def create_record(n=1):
    # for i in range(n):
    #     name=input("enter name ")
    #     age=int(input("enter age "))
    #     height=input("enter height")
    #     l = []
    #     l.append(age)
    #     l.append(height)
    #     d[name] = l

    while True:
        name = input("enter name: ")
        search = d.get(name, False)
        while True:
            age = input("enter age: ")
            if age.isnumeric() and int(age) < 100:
                break
            print("please provide an integer value less than 100")

        if search != False:
            print("user already exist")
            replace = input("do you want to replace it? yes/no")
            if replace.lower().startswith("y"):
                d[name] = int(age)
            else:
                pass
        else:
            d[name] = int(age)
        ques = input("do you want to add more records? enter yes or no: ")
        if ques.lower().startswith('y'):
            continue
        else:
            break

    return None


def get_record():
    name = input("enter the name you want to search: ")
    search_item = d.get(name, False)
    if not search_item:
        print("item does not exist")
    else:
        print(search_item)
    return search_item


def modify_record():
    """
    modifies record in a dictionary
    :return: True if successful else False
    """
    name = input("enter the name of the person you want to modify: ")
    age = input(" enter the new age of the person: ")
    modify = d.get(name, False)
    if modify == False:
        return False
    else:
        d[name] = age
        return True


def delete_record():
    delete_user = input("enter the user you want to be deleted: ")
    search = d.get(delete_user, False)
    if delete_user != False:
        del d[delete_user]
        return True
    else:
        return False


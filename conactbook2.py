contact = {}


def display_contact():
    print(contact.items())
    print("name \t\t contact number")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))


while True:
    choise = int(input("1.ADD NEW CONTACT \n 2.DISPLAY CONTACT \n 3.EDIT CONTACT \n 4.SEARCH CONTACT \n 5 DELETE CONTACT \n 6.EXICT \n ENTER YOUR CHOISE "))
    if choise == 1:
        name = input("enter the contact name")
        phone = input("enter the contact phone")
        contact[name] = phone
    elif choise == 2:
        if not contact:
            print("empty contact book")
        else:
            display_contact()

    elif choise == 3:
        edit_contact = input("enter the contact to be edited")
        if edit_contact in contact:
            phone = input("enter mobile number")
            contact[edit_contact] = phone
            print("contact updated")
            display_contact()
        else:
            print("name is not found in contact book")

    elif choise == 4:
        search_name = input("enter the contact name")
        if search_name in contact:
            print(search_name, "s contact number is", contact[search_name])
        else:
            print("name is not found in contact book")
    elif choise == 5:
        del_contact = input("enter the contact to be deleted")
        if del_contact in contact:
            confirm = input("do you want to deleted this contact yes/no?")
            if confirm == 'yes' or confirm == 'YES':
                contact.pop(del_contact)
            display_contact()
        else:
            print("name is not found in contact book")
    else:
        break

contacts = {}

while True:
    ch = int(input("1. Add Contact\t\t2. View Contact List\n3. Search Contact\t4. Update Contact\n5. Delete Contact\t6. Exit\nEnter Choice: "))
    
    match ch:
        case 1:
            print("\nADD CONTACT")
            mobile_no = int(input("Enter Contact Number: "))
            name = input("Enter Name: ")
            contacts[mobile_no] = name
            print("Contact added successfully")

        case 2:
            print("\nVIEW CONTACT LIST")
            print("Mobile No\tName")
            for k, v in contacts.items():
                print(k, '\t', v)

        case 3:
            ch2 = int(input("1. Search By contact number\t2. Search by name"))
            match ch2:
                case 1:
                    print("\nSEARCH BY CONTACT NUMBER")
                    search_contact = int(input("Enter Contact Number to search: "))
                    if search_contact in contacts:
                        print(f"Name: {contacts[search_contact]}")
                    else:
                        print("Contact not found")
                case 2:
                    print("\nSEARCH BY NAME")
                    search_by_name = input("Enter name to search: ")
                    found = False
                    for mobile_no, name in contacts.items():
                        if search_by_name.lower() in name.lower():
                            print(f"Mobile No: {mobile_no}\tName: {name}")
                            found = True
                    if not found:
                        print("Contact not found")

        case 4:
            ch3 = int(input("1. Update contact by name\t2. Update Contact by number"))
            match ch3:
                case 1:
                    print("\nUPDATE CONTACT BY NAME")
                    search_by_name = input("Enter name to update: ")
                    found = False
                    for mobile_no, name in contacts.items():
                        if search_by_name.lower() in name.lower():
                            new_name = input("Enter new Name: ")
                            contacts[mobile_no] = new_name
                            print("Contact updated successfully")
                            found = True
                    if not found:
                        print("Contact not found")
                case 2:
                    print("\nUPDATE CONTACT BY NUMBER")
                    update_mobile_no = int(input("Enter Contact Number to update: "))
                    if update_mobile_no in contacts:
                        new_name = input("Enter new Name: ")
                        contacts[update_mobile_no] = new_name
                        print("Contact updated successfully")
                    else:
                        print("Contact not found")
                case _:
                    print("Invalid choice for updating contact")
        case 5:
            ch4 = int(input("1.Delete contact by name\t2.Delete contact by number"))
            match ch4:
                case 1:
                    print("\nDELETE CONTACT BY NAME")
                    delete_by_name = input("Enter name to delete: ")
                    found = False
                    for mobile_no, name in contacts.items():
                        if delete_by_name.lower() in name.lower():
                            del contacts[mobile_no]
                            print("Contact deleted successfully")
                            found = True
                    if not found:
                        print("Contact not found")
                case 2:
                    print("\nDELETE CONTACT BY NUMBER")
                    delete_mobile_no = int(input("Enter Contact Number to delete: "))
                    if delete_mobile_no in contacts:
                        del contacts[delete_mobile_no]
                        print("Contact deleted successfully")
                    else:
                        print("Contact not found")
                case _:
                    print("Invalid choice for deleting contact")
        case 6:
            print("Exiting....")
            break

        case _:
            print("Invalid choice. Please enter a valid option.")

        

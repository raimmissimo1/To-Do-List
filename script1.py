print("----------------- Welcome To to do list ----------------- ")

active = True
to_do_list = []

while active:
    print("1.See my To Do List")
    print("2.Add do things")
    print("3.Remove do things")
    print("4.Exit")
    print("--------------------------------------------------------- ")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if not  to_do_list:
            print("To do list is empty")
        num = 1
        for item in to_do_list:
            print(f"{num} : {item}")
            num += 1
    elif choice == 2:
        add_to_do_things = input("Enter what you want to add: ")
        to_do_list.append(add_to_do_things)

    elif choice == 3:
        remove_to_do_things = input("Enter what you want to remove: ")
        if remove_to_do_things in to_do_list:
            to_do_list.remove(remove_to_do_things)
        else:
            print("That was not found.")
    elif choice == 4:
        active = False
        print("Thank you for playing")
my_list = []
my_tuple = ()
my_set = set()
my_dict = {}

while True:
    print("\n1.List 2.Tuple 3.Set 4.Dictionary 5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        print("\n1.Add 2.Remove 3.Display")
        c = int(input("Enter: "))
        if c == 1:
            x = input("Enter element: ")
            my_list.extend(x.split())
        elif c == 2:
            x = input("Enter element: ")
            if x in my_list:
                my_list.remove(x)
            else:
                print("Not found")
        elif c == 3:
            print(my_list)

    elif ch == 2:
        print("\n1.Create 2.Display")
        c = int(input("Enter: "))
        if c == 1:
            data = input("Enter elements: ")
            my_tuple = tuple(data.split())
        elif c == 2:
            print(my_tuple)

    elif ch == 3:
        print("\n1.Add 2.Remove 3.Display")
        c = int(input("Enter: "))
        if c == 1:
            x = input("Enter element: ")
            my_set.add(x)
        elif c == 2:
            x = input("Enter element: ")
            if x in my_set:
                my_set.remove(x)
            else:
                print("Not found")
        elif c == 3:
            print(my_set)

    elif ch == 4:
        print("\n1.Add 2.Remove 3.Display")
        c = int(input("Enter: "))
        if c == 1:
            k = input("Key: ")
            v = input("Value: ")
            my_dict[k] = v
        elif c == 2:
            k = input("Key: ")
            if k in my_dict:
                del my_dict[k]
            else:
                print("Not found")
        elif c == 3:
            print(my_dict)

    elif ch == 5:
        print("Exit")
        break

    else:
        print("Invalid choice")

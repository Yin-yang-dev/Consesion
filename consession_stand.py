def Number_to_word(choice):
    if choice == "1":
        choice = "Pizza"
    elif choice == "2":
        choice = "Nachos"
    elif choice == "3":
        choice = "Popcorn"
    elif choice == "4":
        choice = "Fries"
    elif choice == "5":
        choice = "Chips"
    elif choice == "6":
        choice = "Pretzel"
    elif choice == "7":
        choice = "Soda"
    elif choice == "8":
        choice = "Lemonade"
    return choice




def main():
    leave = False
    My_Menu = {"1: pizza": 5.50,
    "2: nachos": 4.75,
    "3: popcorn": 6.25,
    "4: fires": 3.50,
    "5: chips": 2.00,
    "6: pretzel": 3.50,
    "7: soda": 2.75,
    "8: lemonade": 3.00}
    print(My_Menu)
    keys = My_Menu.keys()
    cart = []
    # for key in My_Menu.keys():
    #     print(key)
    total_cost = 0
    items = My_Menu.items()
    while leave == False:
        print("-----Menu-----")
        for key, value in My_Menu.items():
            print(F"{key}: {value}")
        print("--------------")
        choice = input("choose an item (press q to quit): ")
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("hi")
            item_name = Number_to_word(choice)
            cart.append(item_name)
            total_cost += My_Menu[f"{choice}: {item_name.lower()}"]
            print(Number_to_word("1"))
        elif choice.upper() == "Q":
            print(f"${total_cost}")
            leave = True
        else:
            print("something on the menu")
        

if __name__ == "__main__":
    main()



#if not "potato" in my_menu.keys():
    #print("invalid entry")
#else:
    #add the entry into the cart, use the entry to get the price from the dictionary. 
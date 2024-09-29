def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        while choice not in (1, 2, 3, 4): 
            choice = int(input("Enter your choice: "))

        if choice == 1:
            user_input= input("please enter the item you want to add: ")
            shopping_list.append(user_input)
        elif choice == 2:
            user_input= input("please select the item you want to remove: ")
            if user_input in shopping_list:
                shopping_list.remove(user_input)
            else: 
                print('item not found.')
        elif choice == 3:
            print(shopping_list)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
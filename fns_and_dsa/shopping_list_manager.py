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
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item == "":
                print("No item entered. Nothing was added.")
            else:
                shopping_list.append(item)
                print(f"'{item}' added to the shopping list.")
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item == "":
                print("No item entered. Nothing was removed.")
            else:
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' removed from the shopping list.")
                else:
                    print(f"Item '{item}' not found in the shopping list.")
        elif choice == '3':
            if shopping_list:
                print("Current shopping list:")
                for idx, it in enumerate(shopping_list, start=1):
                    print(f"{idx}. {it}")
            else:
                print("Shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


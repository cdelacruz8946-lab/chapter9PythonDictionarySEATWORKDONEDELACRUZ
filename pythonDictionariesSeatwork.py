record = {}

def add_data():
    key = input("Enter Key: ")
    value = input("Enter Value: ")

    record[key] = value

    print("\nRecord successfully added!")
    print("Current Records:", record)


def delete_data():
    key = input("Enter Key: ")

    if key in record:
        record.pop(key)
        print("\nRecord successfully deleted!")
    else:
        print("\nKey not found!")

    print("Current Records:", record)


def main():
    while True:
        print("\n===== RECORD KEEPING APP =====")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")

        choice = input("Enter your choice: ").lower()

        if choice == "a":
            add_data()

        elif choice == "b":
            delete_data()

        elif choice == "c":
            print("THANK YOU!")
            break

        else:
            print("Invalid choice! Please choose a, b, or c.")


main()
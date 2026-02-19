while True:
    print("\nSimple Menu")
    print("1. Say Hello")
    print("2. Add Two Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello! Keep learning AI 🚀")

    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")

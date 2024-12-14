
def calculator():
    print("\nSimple Calculator")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    
    while True:
        choice = input("\nEnter your choice: ")
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == "1":
                    print(f"Result: {num1 + num2}")
                elif choice == "2":
                    print(f"Result: {num1 - num2}")
                elif choice == "3":
                    print(f"Result: {num1 * num2}")
                elif choice == "4":
                    if num2 != 0:
                        print(f"Result: {num1 / num2}")
                    else:
                        print("Error: Division by zero!")
            except ValueError:
                print("Invalid input! Please enter numbers.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

calculator()

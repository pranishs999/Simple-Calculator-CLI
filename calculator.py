# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user
    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4): "))

            if choice in [1, 2, 3, 4]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == 1:
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == 2:
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == 3:
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == 4:
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid input! Please choose between 1 and 4.")
            
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes' and next_calculation != 'y':
                print("Exiting the calculator............")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")
        
    print("Goodbye! Thanks for using the calculator.")

if __name__ == "__main__":
    main()

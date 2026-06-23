import math

print("=== Scientific Calculator ===")

while True:
    print("\nOperations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Log Base 10")
    print("11. Natural Log (ln)")
    print("12. Factorial")
    print("13. Exit")

    choice = input("Enter choice (1-13): ")

    if choice == "13":
        print("Calculator Closed")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", a + b)
        elif choice == "2":
            print("Result =", a - b)
        elif choice == "3":
            print("Result =", a * b)
        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Result =", a / b)
        elif choice == "5":
            print("Result =", a ** b)

    elif choice == "6":
        x = float(input("Enter number: "))
        print("Result =", math.sqrt(x))

    elif choice == "7":
        x = float(input("Enter angle in degrees: "))
        print("Result =", math.sin(math.radians(x)))

    elif choice == "8":
        x = float(input("Enter angle in degrees: "))
        print("Result =", math.cos(math.radians(x)))

    elif choice == "9":
        x = float(input("Enter angle in degrees: "))
        print("Result =", math.tan(math.radians(x)))

    elif choice == "10":
        x = float(input("Enter number: "))
        print("Result =", math.log10(x))

    elif choice == "11":
        x = float(input("Enter number: "))
        print("Result =", math.log(x))

    elif choice == "12":
        x = int(input("Enter integer: "))
        print("Result =", math.factorial(x))

    else:
        print("Invalid choice")

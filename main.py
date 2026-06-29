while True:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = input("Enter operation (+, -, *, /):q to close the calculator: ")

    if c == "q":
        break

    if c == "+":
        result = a + b
        print(f"The result of {a} + {b} is: {result}")
    elif c == "-":
        result = a - b
        print(f"The result of {a} - {b} is: {result}")
    elif c == "*":
        result = a * b
        print(f"The result of {a} * {b} is: {result}")
    elif c == "/":
        result = a / b if b != 0 else "undefined"
        print(f"The result of {a} / {b} is: {result}")



firstIn = float(input("First number: "))

operator = input("Operator: ")

secondIn = float(input("Second number: "))

if operator == "+":
    print("Sum: {} + {} = {}".format(firstIn, secondIn, firstIn + secondIn))

if operator == "-":
    print("Sum: {} - {} = {}".format(firstIn, secondIn, firstIn - secondIn))

if operator == "/":
    print("Sum: {} / {} = {}".format(firstIn, secondIn, firstIn / secondIn))

if operator == "*":
    print("Sum: {} * {} = {}".format(firstIn, secondIn, firstIn * secondIn))

if operator == "%":
    print("Sum: {} % {} = {}".format(firstIn, secondIn, firstIn % secondIn))

if operator == "//":
    print("Sum: {} // {} = {}".format(firstIn, secondIn, firstIn // secondIn))

if operator == "**":
    print("Sum: {} do potegi  {} = {}".format(firstIn, secondIn, firstIn ** secondIn))
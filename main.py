
#lab 1


#1
def task1(a, b, c):
    if a == b and b == c:
        print(True)
    else:
        print(False)

    print(type(a), hex(id(a)))
    print(type(b), hex(id(b)))
    print(type(c), hex(id(c)))


a = b = c = "Python 2023"
task1(a, b, c)
c = "Java 11"

task1(a, b, c)


#2


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


#3

question1 = ""
question2 = ""
question3 = ""
question4 = ""
question5 = ""
question6 = ""
question7 = ""

lista =[]

for i in range (1-7):
    print()






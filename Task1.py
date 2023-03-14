
# 1
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
import math


def main():
    print("Pythagorean Theorem Calculator!")
    print("this program will solve your hypotinuse: "))
    x = eval(input("enter the a veriable"))
    y = eval(input("B veriable?"))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()

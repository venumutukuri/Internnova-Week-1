def square(n):
    return n * n
def average(a, b, c):
    return (a + b + c) / 3
num = float(input("Enter a number: "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("Square =", square(num))
print("Average =", average(a, b, c))
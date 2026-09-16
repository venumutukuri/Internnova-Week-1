number1=float(input(" Enter a number1:"))
number2=float(input("Enter a number2:"))
print("Addition:",number1+number2)
print("Subtraction:",number1-number2)
print("Multiplication:",number1*number2)
if number2!=0:
    print("Division:",number1/number2)
    print("Modulus:",number1%number2)
else:
    print("Division:Cannot divided by zero")
    print("Modulus: Cannot Calculate  modulus by zero")
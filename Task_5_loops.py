print("Number  from 1 to 20 :")
for i in range(1,21):
    print(i,end=" ")
print("\n")
number=int(input("Enter a number from multiplication table:"))
print(f"\nMultiplication Table of{number}:")
for i in range(1,11):
    print(f"{number} X {i}={number*i}")
print("\n Even numbers from 1 to 50 :")
i=2
while i <= 50:
    print(i,end=" ")
    i+=2
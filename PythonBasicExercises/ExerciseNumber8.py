#Is this number prime?
number = int(input("Write a number: "))

if number == 0 or number == 1:
    print("Your number isn't Prime!")
if number == 2 or number == 3:
    print("Your number is Prime!")
elif number % 2 == 0 or number % 3 == 0:
    print("Your number isn't Prime!")
elif number % 5 == 0 or number % 7 == 0:
    print("Your number isn't Prime!")
else:
    print("Your number is Prime!")
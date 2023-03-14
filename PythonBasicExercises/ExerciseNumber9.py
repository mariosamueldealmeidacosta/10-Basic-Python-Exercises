#The Triangle Area

base = float(input("What's the base of the Triangle: "))
height = float(input("What's the height of the Triangle: "))

if base < 1 or height < 1:
    print("Please write a number higher than 0")
else:
    result = base * height / 2
    print(f"The Triangle area is {result}")

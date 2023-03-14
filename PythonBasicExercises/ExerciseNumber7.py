#BMI Calculator
weight = float(input("What's your weight?(kg) "))
height = float(input("What's your height?(m) "))

BMI = weight / (height * height)
print(f"Your BMI is {BMI:.1f}!")

if BMI < 18.5:
    print("You have a low BMI!")
elif BMI >= 18.5 and BMI <= 24.99: 
    print("You have a regular BMI!")
elif BMI >= 25 and BMI <= 29.99:
    print("You are overweight!")
else:
    print("You are obese!")
#Asks for the user's age and determines whether they are of legal age or not
age = int(input("What's your age? "))

if (age <= 18):
    print("You are underage!")
else:
    print("You are of legal age!")
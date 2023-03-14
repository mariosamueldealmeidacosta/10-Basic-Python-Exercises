#Divisors of a number

number = int(input("Write a number: "))
print("The numbers: ", end="")

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
print(f"are divisible by {number}")
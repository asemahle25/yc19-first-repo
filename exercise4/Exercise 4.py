# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apple", "banana", "cherry", "orange", "grape"]

# TODO: Use a for loop to print each fruit in the list
for fruit in fruits:
  print(fruit) 

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
countdown = 5
while countdown > 0:
   print(countdown)
   countdown += -1
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colors = ["red", "blue", "green", "yellow", "purple"]

# TODO: Use a for loop to select and print 3 random colors from the list
for i in range(3):
    print(random.choice(colors))


#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Import the custom module and use its functions
import math_operations


# TODO: Use a while loop to create a simple calculator
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", math_operations.add(num1, num2))
        elif choice == '2':
            print("Result:", math_operations.subtract(num1, num2))
        elif choice == '3':
            print("Result:", math_operations.multiply(num1, num2))
        elif choice == '4':
            print("Result:", math_operations.divide(num1, num2))
    else:
        print("Invalid input")
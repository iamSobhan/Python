import random

# Set the number of sides on the dice
sides = 6

# Roll the dice
while True:
    roll = random.randint(1, sides)

    # Print the result
    print("You rolled a", roll)

    # Ask the user if they want to roll again
    again = input("Roll again? (y/n): ")
    if again.lower() != "y":
        break

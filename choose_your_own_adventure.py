name = input("Type your Name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a Dirty Road, it has come to end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer == input("You come to a river, you can walk around it or swim accross? Type walk to walk and swim to swim accross: ")

    if answer == "swim":
        print("You swim accross and were eaten by an alligator.")

    elif answer == "walk":

        print("You walked for many miles, ran out of water and you lost the game.")

    else:
        print("Not a valid option. You lose...")


elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose...")

    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the strenger and they give you Diamond. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they offended and you lose.")
        else:
            print("Not a valid option. You lose...")

    else:
        print("Not a valid option. You lose...")

else:
    print("Not a valid option. You lose...")
print("Thank you for trying", name)
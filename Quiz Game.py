print("Welcome to this Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets do that....")
score = 0

answer = input("CPU stands for what? ")

if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("RAM stands for what? ")

if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("GPU stands for what? ")

if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("MB stands for what? ")

if answer.lower() == "mega byte":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("GB stands for what? ")

if answer.lower() == "giga byte":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("Your win ratio " + str((score / 5) * 100) + "%")
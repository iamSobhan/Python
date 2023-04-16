def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

# prompt the user to enter the two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# calculate the HCF
hcf = hcf(num1, num2)

# display the HCF
print("The HCF of", num1, "and", num2, "is", hcf)

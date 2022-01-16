#num = int(input("Enter a Number"))

num = 16
if num < 0:
    print("Enter a Positive Number")
else:
    sum = 0
while(num > 0):
    sum += num
    num -= 1
print("The Sum is", sum)
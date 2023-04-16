def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

# prompt the user to enter the number of terms in the sequence
terms = int(input("Enter the number of terms in the sequence: "))

# display the Fibonacci sequence
if terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci(i))


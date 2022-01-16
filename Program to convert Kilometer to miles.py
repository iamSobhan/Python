#inputs from user

kilometers = float(input("Enter the value of Kilometers: "))

#conversion factor
conv_fac = 0.621371

#calculate miles
miles = kilometers * conv_fac

print('%0.2f kilometers is equal to %0.2f miles' % (kilometers, miles))

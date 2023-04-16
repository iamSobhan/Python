import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# display the calendar for the given month and year
print(calendar.month(year, month))

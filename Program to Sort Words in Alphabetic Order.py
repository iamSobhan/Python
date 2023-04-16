#my_str = "Walter Camp is credited with altering the rules of rugby to create the game of modern North American football we are familiar with today. The line of scrimmage, use of downs, point system, the number of players per side, and the creation of the quarterback position all stemmed from Walter Camp's influence."

# To take input from the user
my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
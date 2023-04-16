def count_vowels(string):
    vowels = 'aeiou'
    vowel_counts = {}
    for vowel in vowels:
        count = string.count(vowel)
        vowel_counts[vowel] = count
    return vowel_counts

string = input("Enter a string: ")
vowel_counts = count_vowels(string)

for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")
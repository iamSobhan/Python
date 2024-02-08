# -*- coding: utf-8 -*-
"""patterns1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tRDaUVsCE7unIkn1sgNDpMUbcK6GoJQt

**1. Pyramid Pattern**
"""

def pyramid_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

pyramid_pattern(5)

"""**2. Inverted Pyramid Pattern**"""

def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

inverted_pyramid(5)

"""**3. Right-angled Triangle Pattern**"""

def right_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

right_triangle(5)

"""**4. Hourglass Pattern**"""

def hourglass(rows):
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for i in range(2, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

hourglass(5)

"""**5. Hollow Pyramid Pattern**"""

def hollow_pyramid(rows):
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            print(" " * (rows - i) + "*" * (2 * i - 1))
        else:
            print(" " * (rows - i) + "*" + " " * (2 * i - 3) + "*")

hollow_pyramid(5)

"""**6. Pyramid with Numbers**"""

def number_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

number_pyramid(5)

"""**7. Butterfly Pattern**"""

def butterfly(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        for j in range(1, 2 * (rows - i) + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

butterfly(5)

"""**8. Diamond Pattern**"""

def diamond(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

diamond(5)

"""**9. Square Pattern**"""

def square_pattern(rows):
    for i in range(rows):
        print("*" * rows)

square_pattern(5)

"""**10. Cross Pattern**"""

def cross_pattern(size):
    for i in range(size):
        for j in range(size):
            if i == size // 2 or j == size // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

cross_pattern(5)

"""**11. Zigzag Pattern**"""

def zigzag_pattern(rows):
    for i in range(1, rows + 1):
        print("*" * i)
    for i in range(rows - 1, 0, -1):
        print("*" * i)

zigzag_pattern(5)

"""**12. Hollow Inverted Pyramid**"""

def hollow_inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        if i == rows or i == 1:
            print("*" * (2 * i - 1))
        else:
            print("*" + " " * (2 * i - 3) + "*")

hollow_inverted_pyramid(5)

"""**13. Rhombus Pattern**"""

def rhombus(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * rows)

rhombus(5)

"""**14. Spiral Pattern**"""

def spiral_pattern(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*", end=" ")
        print()

spiral_pattern(5, 4)

"""**15. Diagonal Star Pattern**"""

def diagonal_star_pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if i == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

diagonal_star_pattern(5)

"""**16. Pyramid with Spaces**"""

def pyramid_with_spaces(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1) + " " * (rows - i))

pyramid_with_spaces(5)

"""**17. Number Triangle**"""

def number_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

number_triangle(5)

"""**18. Heart Pattern**"""

def heart_pattern():
    for i in range(6):
        for j in range(7):
            if (i == 0 and (j == 3 or j == 0 or j == 6)) or \
               (i == 1 and (j == 2 or j == 4)) or \
               (i == 2 and (j == 1 or j == 5)) or \
               (i == 3 and j == 3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

heart_pattern()

"""**19. Pyramid of Alphabets**"""

def alphabet_pyramid(rows):
    start_char = ord('A')
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            char = chr(start_char + j - 1)
            print(char, end=" ")
        print()

alphabet_pyramid(5)

"""**20. Arrow Pattern**"""

def arrow_pattern(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end=" ")
        print()
    for i in range(rows - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

arrow_pattern(5)

"""**21. Christmas Tree**"""

def christmas_tree(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    print(" " * (rows - 1) + "*")

christmas_tree(5)

"""**22. Staircase Pattern**"""

def staircase_pattern(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end=" ")
        print()

staircase_pattern(5)

"""**23. Circular Pattern**"""

import math

def circular_pattern(radius):
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            if math.sqrt(i**2 + j**2) <= radius:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

circular_pattern(5)

"""**24. Diamond Pattern (with Numbers)**"""

def diamond_with_numbers(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * i)

diamond_with_numbers(5)

"""**25. Sine Wave Pattern**"""

import math

def sine_wave_pattern(rows, frequency=1, amplitude=1):
    for i in range(rows):
        spaces = int(amplitude * math.sin(frequency * i) + amplitude)
        print(" " * spaces + "*")

sine_wave_pattern(20, frequency=0.2, amplitude=10)








my_list = [12, 13, 78, 46, 221]

result = list(filter(lambda x: (x % 13 == 0), my_list))

print("The numbers which is divisible by 13 are", result)
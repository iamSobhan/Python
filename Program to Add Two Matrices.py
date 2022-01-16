X = [[12, 13, 4],
    [5, 8, 3],
    [2, 6, 23]]

Y = [[45, 28, 15],
     [63, 33, 34],
     [9, 11, 17]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(X)):   #iterate through row
    for j in range(len(X[0])): #iterate through column
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)


import random

rows, cols = 8,8
A = [[random.randint(3, 4) for _ in range(cols)] for _ in range(rows)]

print('Исходный массив (8x8)')
for row in A:
    print(row)


B =[0,0,0,0,0,0,0,0]
for i in range(rows):
    B[i] = -1
    for j in range(cols):
        if (A[i][j] + A[i][j-1]) == 7:
            B[i] = 1



print('Одномерный массив B:')
print(B)

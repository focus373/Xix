import random

# Шаг 1: Создаём двумерный массив 6x8 со случайными числами (например, от -10 до 10)
rows, cols = 8, 6
A = [[random.randint(-5, 20) for _ in range(cols)] for _ in range(rows)]

# Вывод исходного массива
print("Исходный массив A (8x6):")
for row in A:
    print(row)

# Шаг 2: Формируем одномерный массив B
B = [0,0,0,0,0,0,0,0]
for i in range(rows):
    B[i]=1          
    for j in range(cols):
        if (A[i][j]) < 0:
            B[i]=-1

            

# Вывод результата
print("\nОдномерный массив B:")
print(B)

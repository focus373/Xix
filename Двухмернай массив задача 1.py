import random

# Шаг 1: Создаём двумерный массив 6x8 со случайными числами (например, от -10 до 10)
rows, cols = 6, 8
A = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

# Вывод исходного массива
print("Исходный массив A (6x8):")
for row in A:
    print(row)

# Шаг 2: Формируем одномерный массив B
B = []
for i in range(rows):
    found = False
    for j in range(cols):
        if abs(A[i][j]) > 4:
            B.append(A[i][j])
            found = True
            break
    if not found:
        B.append(0)

# Вывод результата
print("\nОдномерный массив B:")
print(B)

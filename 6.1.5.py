import random
matrix = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
print("Матрица:")
for row in matrix:
    print(row)
diagonal_sum = sum([row[i] for i, row in enumerate(matrix[::-1])])
print("Сумма чисел по диагонали справа налево:", diagonal_sum)

A = [
    [446],
    [465],
    [13],
    [281],
    [432],
    ['error'],
    [80],
    [122],
    [8]
]

for i, row in enumerate(A):
    for j, elem in enumerate(row):
        if isinstance(elem, str):
            A[i][j] = len(elem)
total_sum = sum([elem for row in A for elem in row])
print("Матрица после замены:")
for row in A:
    print(row)

print("Сумма всех элементов матрицы:", total_sum)

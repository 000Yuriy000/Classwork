matrix1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix2 = [[2, 9, 0, 2], [3, 4, 7, 6]]

answer_matrix = [[0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        answer_matrix[i][j] = matrix1[i][j] * matrix2[i][j]

print(answer_matrix)

for i in range(len(answer_matrix)):
    row_sum = sum(answer_matrix[i])
    print(f"{answer_matrix[i]} сумма строки: {row_sum}")
rows = int(input("Введите количество строк: "))
# Ввод количества столбцов
cols = int(input("Введите количество столбцов: "))

# Создание пустого двумерного массива
matrix = []
for i in range(rows):
    row = []  # Пустая строка
    for j in range(cols):
        # Ввод числовых значений элементов
        value = int(input(f"Введите значение элемента [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

# Вывод двумерного массива
print("\nВаш двумерный массив:")
for row in matrix:
    print(row)

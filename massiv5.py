negative_numbers = []
postive_numbers = []
zeros = []
n = int(input("Введите количество чисел: "))
for i in range(n):
    num = input("Введите число: ")
    try:
        num = float(num)
        if num < 0:
            negative_numbers.append(num)
        elif num > 0:
            postive_numbers.append(num)
        else:
            zeros.append(num)
    except ValueError:
        pass

negative_numbers.sort()
postive_numbers.sort()
print("Сумма отрицательных чисел:", sum(negative_numbers))

if len(postive_numbers) > 0:
    average = sum(postive_numbers)
len(postive_numbers)
print("Среднее арифмитическое положительных чисел:", average)
zeros_list = ['*' for _ in zeros]
print(f"Количество элементов списка нулей: {len(zeros)} {zeros_list}")
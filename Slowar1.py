dicttest = {1: 'element 1', 2: 'element 2', 3: 'element 3', 4: 'element 4', 5: 'element 5'}
print("Словарь:", dicttest)
print("Ключи словаря:", dicttest.keys( ))
print("Значения ключей:", dicttest.values( ))
print("Пары (ключи, значения):")
for key, value in dicttest.items( ):
    print(key, ":", value)
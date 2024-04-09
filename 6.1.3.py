
bin_sy = ['11011111', '11011101', '11000111', '11011100', '11011110']
dec_list = [ ]

for binary_num in bin_sy:
    decimal_num = int(binary_num, 2)
    dec_list.append(decimal_num)
    print(decimal_num)

max_num = max(dec_list)
min_num = min(dec_list)

print("Максимальное число:", max_num)
print("Минимальное число:", min_num)

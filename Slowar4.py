double_sy = {1: '10111011', 2: '010101', 3: '11111101', 4: '110010', 5: '011010', 6: '100011001'}
for key in double_sy:
    if key % 2 != 0:
        binary_str = double_sy[key]
        de_num = int(binary_str, 2)
    print(de_num)
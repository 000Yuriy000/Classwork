def punct(txt):
    pu_marks = {'!', '?', '.', ',', '(',')'}
    count = 0
    for char in txt:
        if char in pu_marks:
           count += 1
    return count
input_string = ("(Как дела?)")
output_string = punct(input_string)
print(output_string)

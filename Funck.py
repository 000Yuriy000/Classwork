def upper(t):
    result =""
    for char in t:
        if char.isupper():
            result += char
    return result
input_string = "PriVet"
output_string = upper(input_string)
print(output_string)
test_dict = {'key 1': 'value 1', 'keyyy': 'vlaueee', '123': 123, 'random?': 'yes', 1: 'two'}
value_keyxx = test_dict.get("keyxx")
value_1 = test_dict.get(1)
print("Значения для ключа 'keyxx':", value_keyxx)
print("Значения для ключа 1:", value_1)
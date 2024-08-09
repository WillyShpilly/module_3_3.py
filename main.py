def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(c = False)
print_params(b = 25, c = [1,2,3])

values_list = [777, 'Urban', True]
values_dict = {'a': 123, 'b': 321, 'c': 213}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'string']

print_params(*values_list_2, 42)
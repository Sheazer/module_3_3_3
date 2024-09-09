def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params(1, 99, False)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(True, 3)

values_list = [1,'SS', False]
values_dict = {'a' : 69, 'b' : True, 'c' : 'Tumba'}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32,'String']
print_params(*values_list_2, 42)

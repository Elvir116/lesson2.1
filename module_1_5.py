immutable_var = (1,2,3, "a", "b", "c", [2, 3.5, 7.6], (3, 'ab'))
print(immutable_var)
immutable_var[5] = 10
print(immutable_var[5])
mutable_list = [10,15, "a", "d"]
mutable_list[0] = "dog"
mutable_list[1] = True
mutable_list[2] = 135
print('mutable_list:',mutable_list[2])
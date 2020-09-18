my_list = [1, 1, 8, 2, 6, 8, 0, 9, 4, 2, 5, 8, 3, 5]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)
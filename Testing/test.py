my_list = [70, 32, 98, 88, 92, 36, 81, 83, 87, 66]

print(my_list)

temp = my_list[0]
my_list[1] = my_list[0]
my_list[0] = temp

print(my_list)
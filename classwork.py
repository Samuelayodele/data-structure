number_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 20]
index = 0
while number_list[index:]:
    index += 1
    number_index = index-1
    for number in range(number_index, -1, -1):
        print(number_list[number])




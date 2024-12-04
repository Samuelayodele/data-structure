number = [13, 21, 6, 7, 90]
okpa_list = ['bambara nut', 'maggie', 'palm oil', 'vegetable', 'fish']
print(okpa_list)
okpa_list.append('fish')
print(okpa_list)
ingredient=input('enter ingredient')
for item in okapa_list:
    if item=='ingredient':
        print(item,'is in the list')
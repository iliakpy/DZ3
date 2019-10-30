new_list = []
n = int(input('Введи количество элементов: '))
for i in range(n):
    print('Введи', i + 1, 'элемент: ')
    new_element = int(input())
    new_list.append(new_element)
    new_list.sort()
print(new_list)

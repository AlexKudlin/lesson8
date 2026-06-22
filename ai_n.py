num = int(input('Сколько элементов в массиве?: '))
r = list(map(int, input('Введи массив: ').split()))


last_element = r.pop(-1)  
r.insert(0, last_element)

print(r)
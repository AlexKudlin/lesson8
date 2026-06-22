n = int(input('Сколько элементов в массиве?: '))
r = list(map(int, input('Введи массив: ').split()))

print(r[::-1])
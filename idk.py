m = int(input('Сколько поместиться в лодку рыбаков: '))
n = int(input('Сколько всего рыбаков: '))
wt = list(map(int, input().split(sep=',')))


wt.sort()

boats = 0
easy = 0
heavy = n - 1

while easy <= heavy:
    boats += 1  # Садимся в лодку


    if wt[easy] + wt[heavy] <= m:
        easy += 1  # Садим самого легкого

    heavy -= 1  # Садим самого тяжелого

print(f'Кол-во лодок: {boats}')

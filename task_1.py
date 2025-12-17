times = '1h 45m,360s,25m,30m 120s,2h 60s'
time_in_minutes = 0
#перебираем каждое временное значение в строке times
for time in times.split(','):
    #если по ошибке в строку попало отрицательное значение
    if '-' in time:
        print(f'Задано некорректное временное значение {time}. Оно не будет учитываться в расчетах')
        continue
    #в каждом временном значении выделяем единицу измерения (час, минута, секунда)， переводим в минуты и добавлем к переменной
    for unit in time.split(' '):
        if 'h' in unit:
            time_in_minutes += int(unit.replace('h', '')) * 60
        elif 'm' in unit:
            time_in_minutes += int(unit.replace('m', '')) 
        elif 's' in unit:
            time_in_minutes += int(unit.replace('s', '')) // 60 
print(time_in_minutes)
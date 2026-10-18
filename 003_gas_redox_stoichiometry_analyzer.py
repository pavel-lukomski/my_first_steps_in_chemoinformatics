import math
print('--- Модуль автоматического анализа стехиометрии газовых ОВР ---\n')
total = 0
maximum = 0
minimum = math.inf
i = 1
while i == 1:
    num = int(input('Выберите одну из двух реакций:\n1 - Получение кислорода (2H₂O₂ → 2H₂O + O₂↑)\n2 - Получение углекислого газа (С + O₂ → СO₂↑)\n'))
    
    if str(num) in '12' and len(str(num)) == 1:
        if num == 1:
            m = float(input('Введите массу исходного реагента H₂O₂ в граммах:\n'))
            M = 34
            name = 'кислород'
        elif num == 2:
            m = float(input('Введите массу исходного реагента C в граммах:\n'))
            M = 12
            name = 'углекислый газ'
        n = m / M
        flag = True
    else:
        print('Ошибка: неверный выбор режима данных.')
        flag = False

    if flag == True:
        if num == 1:
            n2 = 0.5 * n
        elif num == 2:
            n2 = n

        V = math.ceil(n2 * 22.4)
        total += V
        maximum = max(maximum, V)
        minimum = min(minimum, V)
        print('Название газа:', name+'. Объём ≈', V, 'дм³')
        i = int(input('1 - продолжить, 2 - завершить цикл\n'))

if total > 500:
    total = str(total)+('!' * (total - 500))
print('Суммарный объём всех выделенных газов за смену ≈', str(total), 'дм³'+'\nМаксимальный объём газа, полученный за один конкретный запуск ≈', str(maximum), 'дм³'+'\nМинимальный объём газа, полученный за один конкретный запуск ≈', str(minimum), 'дм³.')

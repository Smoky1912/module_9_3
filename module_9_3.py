# зададим исх. списки строк
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# создаем генераторную сборку first_result, которая высчитывает разницу длин строк из списков first и second, если их длины не равны
# высчит-т разницу длин строк из задан. списков при том, что длины их не равны
# ф-я zip для перебора строк попарно из двух списков
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# создаем генераторную сборку second_result
# кот. сод.-ит рез-ты сравн. длин строк в одинаковых позициях из списков
# ф-ии range и len для перебора индексов
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# вывод рез-ов
print(list(first_result))
print(list(second_result))
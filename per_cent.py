print()
per_cent = {'ТКБ': 5.6,'СКБ': 5.9,'ВТБ': 4.28,'СБЕР': 4.0}

print('Проценты доходности по вкладам в различных банках: ')
print(per_cent)
print()

money = int(input('Введите сумму вклада: '))
print()

for value in per_cent :
            per_cent[value] =int(per_cent[value] * money / 100)

deposit = list(per_cent.values())
print("Накопленные средства за год вклада в каждом из банков:")
print(deposit)
print()

i=deposit.index(max(deposit))
print("Максимальная сумма, которую вы можете заработать — " + str(deposit[i]))

# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money = 100000
# deposit = [5600, 5900, 4280, 4000]
# Максимальная сумма, которую вы можете заработать — deposit[i]

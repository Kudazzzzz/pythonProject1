per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вложений"))
print(type(money))
dep = list(per_cent.values())
deposit = []
for i in dep:
    deposit.append(i * money)
print(list(map(round, deposit)))
max = int(max(deposit))
print("Максимальная сумма, которую вы можете заработать — ",max)
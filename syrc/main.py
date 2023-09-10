import json
from functions import main_function, check_true



def sort_by_date():
    """
     данная функция работает с данными из operation.json
     сортирует их по порядку (по дате)
     возвращает кортеж с ними
     """
    with open('operations.json', encoding='utf-8') as main_file:
        transactions = json.load(main_file)
        transactions.sort(key=lambda d: d['date'], reverse=True)
    return transactions


all_files = sort_by_date()              # обращаемся к функции сортирующей данные по дате
count = 0
approved = 0
while approved < 5:                      # запускаем цикл, для выборки в 5 транзакций
    file = all_files[count]
    count += 1
    if check_true(file['state']) == False:    # обращаемся к функции, проверяющей прошла ли операция
        continue                              # в случае отмены оп-ии - запускаем цикл далее
    approved += 1
    main_function(file)                      # обращаемся к основной функции, она и выводит данные
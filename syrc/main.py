from functions import main_function, check_true, sort_by_date
import json

with open('operations.json', encoding='utf-8') as main_file:
    transactions = json.load(main_file)
all_files = sort_by_date(transactions)
count = 0
approved = 0
while approved < 5:                      # запускаем цикл, для выборки в 5 транзакций
    file = all_files[count]
    count += 1
    if check_true(file['state']) == False:    # обращаемся к функции, проверяющей прошла ли операция
        continue                              # в случае отмены оп-ии - запускаем цикл далее
    approved += 1
    main_function(file)                      # обращаемся к основной функции, она и выводит данные
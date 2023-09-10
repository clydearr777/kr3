from datetime import datetime
def sort_by_date(transactions):
    """
     данная функция работает с данными из operation.json
     сортирует их по порядку (по дате)
     """
    return transactions.sort(key=lambda d: d['date'], reverse=True)


def coding_numbers(transaction):
    """
     param: transaction - входящие данные карты\счета
     функция перекодирует данные, в случае карты - скрывает в середине цифры звездочками
     в случае счета выдает последние 4 циры номера
     """
    splited = transaction.split()
    a = str(splited[-1])
    if len(a) == 16:
        coded_number = a[0:4]+" "+a[4]+a[5]+"** **** "+a[-4::]
        splited[-1] = coded_number
        coded_number = " ".join(splited)
        return coded_number
    if len(a) == 20:
        coded_number = "**"+a[-4::]
        splited[-1] = coded_number
        coded_number = " ".join(splited)
        return coded_number

def check_transaction(transaction):
    """
    Функция проверяет тип транзакции (Открытие вклада или перевод)
    """
    if transaction == "Открытие вклада":
        return True
    else:
        return False

def check_true(file):
    """
    Принимает 1 набор данных из файла json, проверяет данные по ключу 'state' на предмет
    отменена или прошла операция
    :param file:  набор данных из json
    """
    if file == "CANCELED":
        return False
    else:
        return True

def make_date_readable(data):
    """
    Функция выполняет преобразование даты в формат: ДД.ММ.ГГГГ
    """
    date = datetime.strptime(data,'%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
    return date

def amount(money, valuta):
    """
    функция принимает 2 параметра и обьединяет их в одну строку
    :param money:  сумма переведенных средств в цифрах
    :param valuta:  валюта перевода
    :return:  возвращает данные в нужном нам виде
    """
    return money + " " + valuta


def main_function(file):
    """
    param file: - входящие данные по одной(!) транзакции
    основная функция работает с входщими данными и выдает их в читаемом формате
    так же обращается к вспомогательным функциям: кодировки номера счета\карты,
    проверки типа транзакции, функции преобразования даты в читаемый формат
    """
    true_date = make_date_readable(file['date'])
    if check_transaction(file['description']) == True:
        coding_tr = coding_numbers(file['to'])
        money = amount(file['operationAmount']['amount'], file['operationAmount']['currency']['name'])
        print(true_date, file['description'], '\n',coding_tr,'\n', money,'\n')
    if check_transaction(file['description']) == False:
        coding_tr_from = coding_numbers(file['from'])
        coding_tr_to = coding_numbers(file["to"])
        money = amount(file['operationAmount']['amount'], file['operationAmount']['currency']['name'])
        print(true_date, file['description'], '\n',coding_tr_from, "->", coding_tr_to,"\n", money,"\n")
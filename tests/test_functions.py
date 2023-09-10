from Program.functions import coding_numbers, make_date_readable, check_true, check_transaction, amount

def test_coding_numbers():
    assert coding_numbers("MIR 1234123412366612") == "MIR 1234 12** **** 6612"
    assert coding_numbers("Счет под номером 12341234123412347720") == "Счет под номером **7720"

def test_make_date_readable():
    assert make_date_readable("2019-08-26T10") == "26.08.2019"
    assert make_date_readable("777717717788888999999999") == "77.77.7777"

def test_check_true():
    assert check_true("CANCELED") == False
    assert check_true("EXECUTED") == True

def test_check_transaction():
    assert check_transaction("Перевод частному лицу") == False
    assert check_transaction("Открытие вклада") == True

def test_amount():
    assert amount("1234", "RUBLES") == '1234 RUBLES'
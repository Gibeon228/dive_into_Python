# ### Задание 6
# ***Напишите прогрумму банкомат***
# + Начальная сумма равна 0
# + Допустимые действия: пополнить, снять, выйти
# + Сумма пополнения и снятия кратны 50 у.е.
# + Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# + После каждой третей операции пополнения или снятия начисляются проценты - 3%
# + Нельзя снять больше, чем на счёте
# + При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# + Любое действие выводит сумму денег
bank = 0
count = 0


def add_bank(cash: int):
    global bank
    bank += cash
    global count
    count += 1
    print(f'Сумма на счёте: {bank}')


def take_bank(cash: int):
    global bank
    global count
    if cash <= 2000:
        MIN_COMMISSION = 30
        commission = MIN_COMMISSION
    elif 2000 < cash <= 4000:
        commission = cash * 0.015
    else:
        MAX_COMMISSION = 600
        commission = MAX_COMMISSION
    if bank < cash + commission:
        print(f'Недостаточно денег на счёте')
        print(f'Сумма на счёте: {bank}')
        return
    bank -= cash
    print(f'Сумма на счёте: {bank}')
    count += 1


def exit_bank():
    global bank
    print(f'Сумма на счёте: {bank}')
    exit()


def check_bank():
    cash = int(input('Введите сумму для снятия'))
    if cash % 50 == 0:
        return cash
    check_bank()

while True:
    if bank > 5_000_000:
        bank *= 0.9
    action = input('1 - снять\n2 - пополнить\n3 - выйти\n')
    match action:
        case '1':
            take_bank(check_bank())
        case '2':
            add_bank(check_bank())
        case '3':
            exit_bank()
    if count == 3:
        bank *= 1.03
        count = 0

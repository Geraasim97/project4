
def check_wallet(where: str):
    '''
    Функция шифрует данные кошелька, в зависимости от его типа:
    Счет или Карта
    :param where: указатель положение кошелька в счете (получатель:to или отправитель:from)
    :return: зашифрованный кошелек
    '''
    wallet = "Неизвестно"


    try:
        card = inf[f'{where}']
        if card[:4] == "Счет":
            wallet = f"{card[:4]} **{card[-4:]}"
        else:
            wallet = f"{card[:-12]} {card[-12:-10]}** **** {card[-4:]}"
        return wallet
    except:
        return wallet
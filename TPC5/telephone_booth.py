import sys
import re


def main():
    re_pick_up = re.compile("LEVANTAR")
    re_abort = re.compile("ABORTAR")

    re_tel_number = re.compile(r'T=(?P<number>\d+)')

    balance = 0.0

    on = True
    while on:
        operation = sys.stdin.readline()

        if re_pick_up.match(operation):
            balance = process_pick_up(balance)

            print(balance)
            print("end")
            on = False

    pass


def process_pick_up(balance):
    re_coin_list = re.compile(r'MOEDA (?P<coins>(\d+[e|c]\s?)+)')

    coin_input = input("Introduza moedas.\n")

    coin_list = re_coin_list.match(coin_input)
    # processes a valid coin list

    if coin_list:
        coins = filter_coins(coin_list)

        balance += compute_amount(coins)

        print_invalid_coins(coins)

    return balance


def print_invalid_coins(coins):
    invalid_coins = "Moeda inválida - "

    if len(coins['invalid']) > 0:

        for invalid_coin in coins['invalid']:
            invalid_coins += invalid_coin + ' '

    print(invalid_coins)


def filter_coins(coin_list):
    coins = {
        'valid': [],
        'invalid': []
    }

    re_valid_coin = re.compile(r'(10c|20c|50c|1e|2e)')
    re_coin = re.compile(r'(?P<value>\d{1,2})(?P<type>[c|e])')

    # filters valid coins from invalid ones
    for coin in re.split(r'\s', coin_list.group('coins')):

        if re_valid_coin.match(coin):
            coins['valid'].append(re_coin.match(coin))
        else:
            coins['invalid'].append(coin)

    return coins


def compute_amount(coins):
    amount = 0.0
    for coin in coins['valid']:
        value = float(coin.group('value'))

        if coin.group('type') == 'e':
            amount += value
        else:
            amount += value * 0.01
    return amount


if __name__ == "__main__":
    main()

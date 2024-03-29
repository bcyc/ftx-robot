from ftx.client import FtxClient
import datetime
from traceback import format_exc

LEND_COINS = ['ETH', 'USD', 'BTC']

def auto_lending(client: FtxClient) -> None:
    print('[auto_lending] DEBUG: {}'.format(datetime.datetime.now()))
    for coin in LEND_COINS:
        print('[auto_lending] DEBUG: start lending {}'.format(coin))
        lend_coin(client, coin)

def lend_coin(client: FtxClient, coin: str) -> None:
    print('[lend_coin] DEBUG: {}'.format(datetime.datetime.now()))
    balance_coin = client.get_margin_lending_info_coin(coin)
    if balance_coin is None:
        return
    if coin in ['USD']:
        available_balance = float(format(balance_coin['lendable'], '.6f')) - 0.000001
    else:
        available_balance = float(format(balance_coin['lendable'] * 0.85, '.6f'))
    lend_rate = client.get_margin_lending_rate_coin(coin)
    lend_rate['estimate'] -= 0.00000001
    if available_balance > 0:
        print('Lending coin: {}, size: {}, rate: {}'.format(coin, available_balance, lend_rate['estimate']))
        try:
            client.lends(coin=coin, size=available_balance, rate=lend_rate['estimate'])
        except:
            print(format_exc())

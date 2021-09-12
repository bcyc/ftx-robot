from ftx.client import FtxClient
from traceback import format_exc
import datetime

STAKE_COINS = ['SOL']

def auto_staking(client: FtxClient) -> None:
    print('[auto_staking] DEBUG: {}'.format(datetime.datetime.now()))
    for coin in STAKE_COINS:
        stake_coin(client, coin)

def stake_coin(client: FtxClient, coin: str) -> None:
    balance_coin = client.get_balance_coin(coin)
    if balance_coin is None:
        return
    available_balance = balance_coin['availableWithoutBorrow']
    print('[stake_coin] DEBUG: balance = {}'.format(balance_coin))
    if available_balance > 0:
        try:
            print('[stake_coin] DEBUG: coin = {}, size = {}'.format(coin, available_balance))
            print(client.stakes(coin=coin, size=available_balance))
        except:
            print(format_exc())
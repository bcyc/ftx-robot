from ftx.client import FtxClient


STAKE_COINS = ['SOL']


def auto_staking(client: FtxClient) -> None:
    for coin in STAKE_COINS:
        stake_coin(client, coin)


def stake_coin(client: FtxClient, coin: str) -> None:
    balance_coin = client.get_balance_coin(coin)
    if balance_coin is None:
        return
    available_balance = balance_coin['free']
    print('[stake_coin] DEBUG: balance = {}'.format(balance_coin))
    if available_balance > 0:
        client.stakes(coin=coin, size=available_balance)

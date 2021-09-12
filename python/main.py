import schedule, time
from ftx.client import FtxClient
from staking import auto_staking
from lending import auto_lending
from settings import LENDING, MAIN


def main() -> None:
    lendingClient = FtxClient(api_key=LENDING['API'],
                       api_secret=LENDING['SECRET'],
                       subaccount_name=LENDING['SUBACCOUNT'])
    stakingClient = FtxClient(api_key=MAIN['API'],
                       api_secret=MAIN['SECRET'],
                       subaccount_name=MAIN['SUBACCOUNT'])
    auto_lending(lendingClient)
    auto_staking(stakingClient)
    schedule.every().hour.at(":59").do(auto_lending, lendingClient)
    schedule.every().hour.at(":40").do(auto_staking, stakingClient)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()

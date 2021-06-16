import schedule, time
from ftx.client import FtxClient
# from staking import auto_staking
from lending import auto_lending
from settings import API, SECRET, SUBACCOUNT


def main() -> None:
    client = FtxClient(api_key=API,
                       api_secret=SECRET,
                       subaccount_name=SUBACCOUNT)
    auto_lending(client)
    schedule.every().hour.at(":58").do(auto_lending, client)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()

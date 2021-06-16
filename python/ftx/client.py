# https://github.com/ftexchange/ftx/blob/master/rest/client.py
import time
import urllib.parse
from typing import Optional, Dict, Any, List

from requests import Request, Session, Response
import hmac


class FtxClient:
    _ENDPOINT = 'https://ftx.com/api/'

    def __init__(self, api_key=None, api_secret=None,
                 subaccount_name=None) -> None:
        self._session = Session()
        self._api_key = api_key
        self._api_secret = api_secret
        self._subaccount_name = subaccount_name

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request('GET', path, params=params)

    def _post(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request('POST', path, json=params)

    def _delete(self, path: str,
                params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request('DELETE', path, json=params)

    def _request(self, method: str, path: str, **kwargs) -> Any:
        request = Request(method, self._ENDPOINT + path, **kwargs)
        self._sign_request(request)
        response = self._session.send(request.prepare())
        return self._process_response(response)

    def _sign_request(self, request: Request) -> None:
        ts = int(time.time() * 1000)
        prepared = request.prepare()
        signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode(
        )
        if prepared.body:
            signature_payload += prepared.body
        signature = hmac.new(self._api_secret.encode(),
                             signature_payload, 'sha256').hexdigest()
        request.headers['FTX-KEY'] = self._api_key
        request.headers['FTX-SIGN'] = signature
        request.headers['FTX-TS'] = str(ts)
        if self._subaccount_name:
            request.headers['FTX-SUBACCOUNT'] = urllib.parse.quote(
                self._subaccount_name)

    def _process_response(self, response: Response) -> Any:
        try:
            data = response.json()
        except ValueError:
            response.raise_for_status()
            raise
        else:
            if not data['success']:
                raise Exception(data['error'])
            return data['result']

    def get_balances(self) -> List[dict]:
        return self._get('wallet/balances')

    def get_balance_coin(self, coin: str) -> dict:
        balance_coin = [balance for balance in self.get_balances()
                        if balance['coin'] == coin]
        if balance_coin == []:
            return None
        return balance_coin[0]

    def get_margin_lending_info(self) -> List[dict]:
        return self._get('spot_margin/lending_info')

    def get_margin_lending_info_coin(self, coin: str) -> dict:
        lending_info_coin = [lending_info for lending_info in self.get_margin_lending_info()
                        if lending_info['coin'] == coin]
        if lending_info_coin == []:
            return None
        return lending_info_coin[0]

    def get_margin_lending_rate(self) -> List[dict]:
        return self._get('spot_margin/lending_rates')

    def get_margin_lending_rate_coin(self, coin: str) -> dict:
        lending_rate_coin = [lending_rate for lending_rate in self.get_margin_lending_rate()
                        if lending_rate['coin'] == coin]
        if lending_rate_coin == []:
            return None
        return lending_rate_coin[0]

    def stakes(self, coin: str, size: float) -> dict:
        return self._post(f'srm_stakes/stakes', {'coin': coin, 'size': size})

    def get_stake_balances(self) -> dict:
        return self._get(f'staking/balances')

    def lends(self, coin: str, size: float, rate: float) -> dict:
        return self._post(f'spot_margin/offers', {'coin': coin, 'size': size, 'rate': rate})
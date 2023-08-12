import logging

import requests


class Client:
    def __init__(self, token=None):
        self.token = token
        self.requests_timeout = 3
        self.base_url = "https://api.spacetraders.io/v2"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.session = requests.Session()

    def send(
        self, method, endpoint, auth=True, headers=None, data=None, **kwargs
    ):
        url = self.base_url + endpoint
        head = self.headers
        if auth:
            head["Authorization"] = f"Bearer {self.token}"
        if isinstance(headers, dict):
            head.update(headers)

        match method.lower():
            case "get":
                response = self._get(url, headers=head, **kwargs)
            case "post":
                response = self._post(url, headers=head, data=data, **kwargs)

        if response.status_code == 204:
            response_data = {}
        else:
            response_data = response.json()

        if response.status_code == 429:
            # TODO handle rate limiting
            pass

        if "error" in response_data.keys():
            print(
                f"ERROR {response_data['error']['code']}: "
                f"{response_data['error']['message']}"
            )
        return response_data

    def _get(
        self, url: str, headers: dict | None = None, **kwargs
    ) -> requests.Response:
        r = self.session.get(url, headers=headers, **kwargs)
        logging.info(r.content)
        return r

    def _post(
        self,
        url: str,
        headers: dict | None = None,
        data: dict | None = None,
        **kwargs,
    ) -> requests.Response:
        r = self.session.post(url, headers=headers, json=data, **kwargs)
        logging.info(r.content)
        return r

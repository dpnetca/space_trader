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

        return response

    def _get(self, url, headers=None, **kwargs):
        # r = requests.get(url, headers=headers, **kwargs)
        r = self.session.get(url, headers=headers, **kwargs)
        logging.info(r.content)
        if r.status_code == 204:
            return r.content
        r_data = r.json()
        if "error" in r_data.keys():
            print(
                f"ERROR {r_data['error']['code']}: "
                f"{r_data['error']['message']}"
            )
        return r_data

    def _post(self, url, headers=None, data=None, **kwargs):
        # r = requests.post(url, headers=headers, json=data, **kwargs)
        r = self.session.post(url, headers=headers, json=data, **kwargs)
        logging.info(r.content)
        r_data = r.json()
        if "error" in r_data.keys():
            print(
                f"ERROR {r_data['error']['code']}: "
                f"{r_data['error']['message']}"
            )
        return r_data

import requests


class SpaceTraders:
    def __init__(self, token=None):
        self.requests_timeout = 3
        self.base_url = "https://api.spacetraders.io/v2"
        self.token = token

    def send(self, method, url, data=None):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        match method.lower():
            case "get":
                response = requests.get(
                    url, headers=headers, timeout=self.requests_timeout
                )
            case "post":
                response = requests.post(
                    url,
                    headers=headers,
                    timeout=self.requests_timeout,
                    json=data,
                )

        # TODO handle the response for errors etc.

        return response.json()

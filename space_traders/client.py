import requests


class Client:
    def __init__(self, token=None):
        self.token=token
        self.requests_timeout = 3
        self.base_url = "https://api.spacetraders.io/v2"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def send(self, method, endpoint, auth=True, headers=None, data=None, **kwargs):
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
                pass
            
        return response
    
    def _get(self, url, headers=None, **kwargs):
        r = requests.get(url, headers=headers, **kwargs)
        return r.json()

    def _post(self, url, headers=None, data=None, **kwargs):
        r = requests.post(url, headers=headers, json=data **kwargs)
        return r.json()


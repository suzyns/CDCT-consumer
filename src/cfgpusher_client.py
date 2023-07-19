import requests


class CfgpusherClient(object):
    def __init__(self, base_uri: str):
        self.base_uri = base_uri

    def get_file(self, filepath: str):
        resp = requests.get(f"{self.base_uri}/file/{filepath}")
        if resp.status_code == 404:
            return resp.json()
        return resp.text

    def write_file(self, filepath: str, content: str):
        return requests.post(f"{self.base_uri}/file/{filepath}", data=content).json()
    
    def delete_file(self, filepath: str):
        return requests.delete(f"{self.base_uri}/file/{filepath}").json()

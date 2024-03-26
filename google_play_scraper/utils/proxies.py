from abc import ABC, abstractmethod

class Proxy(ABC):
    def __init__(self, username: str, password: str, host: str, port: int):
        self.username = username
        self.password = password
        self.host = host
        self.port = port

    @abstractmethod
    def get_proxy(self) -> dict:
        """
        Abstract method to get the proxy information.

        Returns:
        - proxy (dict): Dictionary containing proxy information.
        """
        pass


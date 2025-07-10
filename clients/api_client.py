from abc import ABC, abstractmethod


class APIClient(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get_client(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

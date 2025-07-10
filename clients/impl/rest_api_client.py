from logging import Logger
from clients.api_client import APIClient
import requests
from requests import Session


class RestApiClient(APIClient):
    _session: Session = None

    def __init__(self):
        self._logger = Logger("rest_api_client")

    def create(self):
        RestApiClient._session = Session()
        self._logger.info("Rest API Client session created")

    def get_client(self):
        if RestApiClient._session:
            self._logger.info("Returning Rest API Client with session")
            return RestApiClient._session
        self._logger.info("Returning Rest API Client without session")
        return requests

    def destroy(self):
        if RestApiClient._session:
            RestApiClient._session.close()
            RestApiClient._session = None
            self._logger.info("Rest API Client session destroyed")

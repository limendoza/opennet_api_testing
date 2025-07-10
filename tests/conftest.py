import csv
import os
import pytest
from clients.impl.rest_api_client import RestApiClient
from utils.logger import Logger

Logger.initialize_logger("api_testing")


@pytest.fixture
def rest_api_client():
    rest_api_client = RestApiClient()
    client = rest_api_client.get_client()
    yield client
    rest_api_client.destroy()


@pytest.fixture
def base_url():
    yield "https://v6.exchangerate-api.com/v6"


@pytest.fixture
def auth_header():
    yield {"Authorization": f"Bearer {os.environ["api_key"]}"}


def get_test_data(file_path: str):
    test_data = []
    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)
        for row in csv_reader:
            test_data.append(row)
    return test_data

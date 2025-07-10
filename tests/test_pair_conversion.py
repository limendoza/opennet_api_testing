import requests
import pytest

from tests.conftest import get_test_data
from utils.logger import Logger


@pytest.fixture
def base_path(base_url):
    yield base_url + "/pair"


log = Logger.create_logger("test_pair_conversion")


class TestPairConversion:

    @pytest.mark.parametrize("test_data", get_test_data("resources/test_data/pair_conversion/positive/pair_conversion.csv"), ids=lambda x: x[0])
    def test_pair_conversion(self, test_data, rest_api_client: requests, base_path: str, auth_header: dict):
        name, base_currency, target_currency = tuple(test_data)
        log.info(f"Pair conversion from {name}")
        response = rest_api_client.get(
            f"{base_path}/{base_currency}/{target_currency}", headers=auth_header)

        conversion_rate = response.json().get("conversion_rate")
        log.info(
            f"{name} current rate is {conversion_rate}")
        assert response.status_code == 200
        assert response.json()["result"] == "success"
        assert conversion_rate

    @pytest.mark.parametrize("test_data", get_test_data("resources/test_data/pair_conversion/positive/pair_conversion_with_amount.csv"), ids=lambda x: x[0])
    def test_pair_conversion_with_amount(self, test_data, rest_api_client: requests, base_path: str, auth_header: dict):
        name, base_currency, target_currency, amount = tuple(test_data)
        log.info(f"Pair conversion from {name} with amount of {amount}")
        response = rest_api_client.get(
            f"{base_path}/{base_currency}/{target_currency}/{amount}", headers=auth_header)

        conversion_rate = response.json().get("conversion_rate")
        conversion_result = response.json().get("conversion_result")
        log.info(
            f"{name} current rate is {conversion_rate}")
        assert response.status_code == 200
        assert response.json()["result"] == "success"
        assert conversion_result
        assert round(float(amount) * conversion_rate, 4) == conversion_result

    @pytest.mark.parametrize("test_data", get_test_data("resources/test_data/pair_conversion/negative/pair_conversion.csv"), ids=lambda x: x[0])
    def test_pair_conversion_with_unknown_currency_codes(self, test_data, rest_api_client: requests, base_path: str, auth_header: dict):
        name, base_currency, target_currency = tuple(test_data)
        log.info(f"Pair conversion from {name}")
        response = rest_api_client.get(
            f"{base_path}/{base_currency}/{target_currency}", headers=auth_header)

        assert response.status_code == 404
        assert response.json()["result"] == "error"
        assert response.json()["error-type"] == "unsupported-code"

    @pytest.mark.parametrize("test_data", get_test_data("resources/test_data/pair_conversion/negative/pair_conversion_with_amount.csv"), ids=lambda x: x[0])
    def test_pair_conversion_with_negative_amount(self, test_data, rest_api_client: requests, base_path: str, auth_header: dict):
        name, base_currency, target_currency, amount = tuple(test_data)
        log.info(f"Pair conversion from {name} with amount of {amount}")
        response = rest_api_client.get(
            f"{base_path}/{base_currency}/{target_currency}/{amount}", headers=auth_header)

        assert response.status_code == 404  # API returns not found for negative values

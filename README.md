# API Testing

## Setup
- Create python virtual environment `python -m venv .venv`.
- Initialize virtual environment `source .venv/bin/activate`.
- Install dependencies `pip install -r requirements.txt`.
- Create an account and get free api key from [Exchange Rate API](https://www.exchangerate-api.com/).
- Set the `api_key` as environment variable.

## Tests
The project current consists of the following test:
- Test pair conversion
- Test pair conversion with amount
- Test pair conversion with unknown currency codes
- Test pair conversion with negative amount

To run the tests in the current project just simply execute `pytest` in the terminal.

## Structure
```
.
├── clients
│   ├── api_client.py
│   └── impl
│       └── rest_api_client.py
├── README.md
├── requirements.txt
├── resources
│   └── test_data
│       └── pair_conversion
│           ├── negative
│           │   ├── pair_conversion.csv
│           │   └── pair_conversion_with_amount.csv
│           └── positive
│               ├── pair_conversion.csv
│               └── pair_conversion_with_amount.csv
├── tests
│   ├── conftest.py
│   └── test_pair_conversion.py
└── utils
    └── logger.py
```
- `clients` contains the api clients to be used in the project.
- `requirements.txt` contains a list of required module for the project.
- `resources` contains the files that are used and also generated from the project.
- `tests` contains the test details.
- `utils` contains the utilities that can be used across the project.

## Test cases
| Test case | Base Currency | Target Currency |
| ----------- | ----------- | ----------- |
| Convert a pair of currencies | USD | EUR |
| Convert a pair of currencies with unknown currency codes | ABC | TXT |

| Test case | Base Currency | Target Currency | Amount |
| ----------- | ----------- | ----------- | ----------- |
| Convert a pair of currencies with amount | AED | USD | 100 |
| Convert a pair of currencies with negative amount | MYR | IDR | -34 |
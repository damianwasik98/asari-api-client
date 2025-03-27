# asari-api-client

API client for [Asari CRM](https://asaricrm.com/).

For now I've added only a few endpoints which I needed for automation.

## Installation

```sh
pip install asari-api-client
```

## Tests

There are only integration tests for authentication to crm.
To run them you need to use your account (because I don't have dedicated account for testing).

Before running tests you'll need to export asari credentials as env variables:
```sh
export ASARI_EMAIL="valid email"
export ASARI_PASSWORD="valid password"
```

```sh
pytest tests
```

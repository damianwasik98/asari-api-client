# asari-api-client

API client for [Asari CRM](https://asaricrm.com/).

For now I've added only a few endpoints which I needed for automation.

## Tests

There are only integration tests for authentication do crm.
To run them you need to use your account (because I don't have dedicated account for testing).
Before running tests export asari credentials as env variables [checkout which variables in the test file](./tests/integration/test_authenticate.py)

```sh
pytest tests
```

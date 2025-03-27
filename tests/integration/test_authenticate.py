import os

import pytest

from asari.auth import authenticate
from asari.exceptions import AsariAuthenticationError


def test_returns_session_id_when_credentials_are_correct() -> None:
    email = os.environ["ASARI_EMAIL"]
    password = os.environ["ASARI_PASSWORD"]

    result = authenticate(email, password)
    assert isinstance(result, str)


def test_raises_when_credentials_are_incorrect() -> None:
    email = "invalid@example.com"
    password = "bad_password123"

    with pytest.raises(AsariAuthenticationError):
        authenticate(email, password)

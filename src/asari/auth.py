from asari import consts
import requests
from requests import Response

from asari.exceptions import AsariAuthenticationError


def authenticate(email: str, password: str) -> str:
    url: str = f"{consts.BASE_URL}/login/authenticate"
    payload: str = f"email={email}&password={password}"

    headers: dict[str, str] = {
        "origin": "https://login.asari.pro",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "navigate",
        "sec-fetch-dest": "document",
        "referer": "https://login.asari.pro/",
    }
    response: Response = requests.post(
        url=url, data=payload, headers=consts.HEADERS | headers
    )
    failed = False
    if response.status_code != 200:
        failed = True
    elif (
        response.history[-1].headers["Location"]
        == "https://k2.asari.pro/userBase/authfail"
    ):
        failed = True

    if failed:
        raise AsariAuthenticationError("Login failed")

    return response.history[0].cookies["JSESSIONID"]

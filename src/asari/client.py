import requests
from requests import Response

from asari import consts
from asari.auth import authenticate


class AsariAPI:
    def __init__(self, email: str, password: str) -> None:
        self._session_id: str = authenticate(email, password)
        self._cookies: dict[str, str] = {"JSESSIONID": self._session_id}

    def find_locations(
        self, name: str, page: int = 1, start: int = 0, limit: int = 25
    ) -> dict:
        url: str = f"{consts.BASE_URL}/api/apiLocation/findLocations"
        params: dict = {
            "query": name,
            "page": page,
            "start": start,
            "limit": limit,
        }
        headers: dict[str, str] = {
            "dnt": "1",
            "priority": "u=1, i",
            "referer": "https://k2.asari.pro/index.html",
            "sec-ch-ua": '"Not:A-Brand";v="24", "Chromium";v="134"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "macOS",
            "sec-fetch-dest": "empty",
            "x-requested-with": "XMLHttpRequest",
        }
        response: Response = requests.get(
            url=url,
            params=params,
            headers=consts.HEADERS | headers,
            cookies=self._cookies,
        )
        return response.json()

    def create_contact(
        self,
        first_name: str,
        last_name: str | None = None,
        phone_number: str | None = None,
        phone_description: str | None = None,
    ) -> dict:
        url = f"{consts.BASE_URL}/api/apiCustomer/create"
        payload: dict = {
            "id": "",
            "firstName": first_name or "",
            "lastName": last_name or "",
            "phones[0].phoneNumber": phone_number or "",
            "phones[0].description": phone_description or "",
            "phones[0].phoneType": "Other",
            "phones[0].toBeDeleted": "false",
            "emails[0].email": "",
            "emails[0].toBeDeleted": "false",
            "documentNo": "",
            "personIdCode": "",
            "registerId": "",
            "parentCompany.id": "",
            "position": "",
            "source": "",
            "assignedTo.id": "",
            "address.country.id": "",
            "address.stateOrProvince": "",
            "address.city": "",
            "address.postalCode": "",
            "address.fullStreet": "",
            "agreToTradeInformation": "",
            "note": "",
            "customerType": "Person",
        }
        headers: dict[str, str] = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "dnt": "1",
            "origin": "https://k2.asari.pro",
            "priority": "u=1, i",
            "referer": "https://k2.asari.pro/index.html",
            "sec-ch-ua": '"Not:A-Brand";v="24", "Chromium";v="134"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "x-requested-with": "XMLHttpRequest",
        }
        response: Response = requests.post(
            url=url,
            data=payload,
            headers=consts.HEADERS | headers,
            cookies=self._cookies,
        )
        return response.json()

    def create_sale(
        self,
        location_id: int,
        customer_id: int,
        description: str | None = None,
        private_description: str | None = None,
        area_min: int | None = None,
        area_max: int | None = None,
        price_min: int | None = None,
        price_max: int | None = None,
        no_of_rooms_min: int | None = None,
        no_of_rooms_max: int | None = None,
        floor_no_min: int | None = None,
        floor_no_max: int | None = None,
        price_m2_min: int | None = None,
        price_m2_max: int | None = None,
        year_built_min: int | None = None,
        year_built_max: int | None = None,
    ) -> dict:
        url: str = f"{consts.BASE_URL}/api/apiSeeker/create"

        headers: dict[str, str] = {
            "accept": "application/json",
            "origin": "https://k2.asari.pro",
            "x-requested-with": "XMLHttpRequest",
            "referer": "https://k2.asari.pro/index.html",
            "sec-fetch-dest": "empty",
        }

        payload: dict = {
            "listingFilter.geoPolygon": "[]",
            "section": "ApartmentSale",
            "id": "",
            "listingFilter.locations": str(location_id),
            "listingFilter.locationsExcepted": "",
            "process.id": "",
            "listingFilter.mortgageMarket": "",
            "listingFilter.totalAreaMin": area_min or "",
            "listingFilter.totalAreaMax": area_max or "",
            "listingFilter.totalAreaSearchRangePercentMinus": "",
            "listingFilter.totalAreaSearchRangePercentPlus": "",
            "listingFilter.priceMin": price_min or "",
            "listingFilter.priceMax": price_max or "",
            "listingFilter.priceCurrency": "PLN",
            "listingFilter.priceSearchRangePercentMinus": "",
            "listingFilter.priceSearchRangePercentPlus": "",
            "listingFilter.priceM2Min": price_m2_min or "",
            "listingFilter.priceM2Max": price_m2_max or "",
            "listingFilter.noOfRoomsMin": no_of_rooms_min or "",
            "listingFilter.noOfRoomsMax": no_of_rooms_max or "",
            "listingFilter.floorNoMin": floor_no_min or "",
            "listingFilter.floorNoMax": floor_no_max or "",
            "listingFilter.yearBuiltMin": year_built_min or "",
            "listingFilter.yearBuiltMax": year_built_max or "",
            "listingFilter.vacantFromDateMin": "",
            "listingFilter.vacantFromDateMax": "",
            "seekerRating": "",
            "provisionAmount": "",
            "description": description,
            "privateDescription": private_description,
            "emailingType": "None",
            "emailingScope": "Company",
            "customer.id": customer_id,
            "contract.id": "",
            "additionalCustomers": "",
        }

        response = requests.post(
            url=url,
            data=payload,
            headers=consts.HEADERS | headers,
            cookies=self._cookies,
        )
        return response.json()

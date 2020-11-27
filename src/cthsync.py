import requests

from settings import *
from square.client import Client as SquareClient


"""
    Untapped for Business API documentation
    https://docs.business.untappd.com/, https://docs.business.untappd.com/#errors
    API Structure:
    ->current_user
    ->container_sizes
    ->locations
        ->social_announcements
        ->historical_items
        ->hours
        ->insights
        ->events
        ->custom_menus
            ->custom_sections
                ->...
        ->menus
            ->sections
                ->items
                    ->containers
"""


class CTHSync:
    """
    This class should encapsulate the functionality for syncing changes made in Square
    to the corresponding data in Untappd For Business.
    """

    def __init__(self):
        """
        Create an instance of all needed Client APIs and initialize with the credentials
        from the project settings.
        """
        # Configure Square settings
        self.square_client = SquareClient(
            access_token=secure_settings.get("square", {}).get("access_token"),
            environment="sandbox",
        )

        # Configure Untappd For Business settings
        ufb_secure = secure_settings.get("ufb", {})
        # Some problem with the encoding below...FIXME
        # token = f'{ufb_secure.get("access_email")}:{ufb_secure.get("access_token_rw")}'
        # encoded_token = b64encode(token.encode("ascii")).decode()

        encoded_token = ufb_secure.get("base64_ro")  # Pre-encoded value
        self.ufb_headers = {"Authorization": f"Basic {encoded_token}"}
        self.ufb_api = settings.get("ufb", {}).get("api_root")

    def list_square_inventory_counts(self) -> dict:
        body = {}
        result = self.square_client.inventory.batch_retrieve_inventory_counts(body)
        return result.body if result.is_success() else f"Error: {result.errors}"

    def list_square_locations(self) -> dict:
        """
        Get locations defined for this Square account, 'body' is the list of locations
        :return:
        """
        result = self.square_client.locations.list_locations()
        return result.body if result.is_success() else result.errors

    def update_square_location(self, loc_id: str = None, loc_data: dict = None):
        result = self.square_client.locations.update_location(loc_id, loc_data)
        return result.body if result.is_success() else f"Error: {result.errors}"

    def list_ufb_locations(self):
        ufb = requests.get(self.ufb_api + "locations", headers=self.ufb_headers)
        return ufb.json() if ufb.status_code == 200 else ufb.status_code

    def list_ufb_container_sizes(self):
        ufb = requests.get(self.ufb_api + "container_sizes", headers=self.ufb_headers)
        return ufb.json() if ufb.status_code == 200 else ufb.status_code

    def update_ufb_location(self, loc_id: int = None, loc_data: dict = None):
        """
        id	Integer	true	The id of the location.
        mailing_address1	String	false	The location mailing street address.
        mailing_address2	String	false	The location mailing address (PO Box, Apt, Ste, etc.)
        mailing_city	String	false	The location mailing city
        mailing_postcode	String	false	The location mailing postcode
        mailing_region	String	false	The location mailing state/region
        mailing_country	String	false	The location mailing country

        e.g. { "location": { "mailing_address1": "123 Bourbon St" } }
        :param loc_id:
        :param loc_data:
        :return:
        """
        pass

    def update_ufb_location_details(self, loc_id: int = None, loc_data: dict = None):
        """
        PUT /locations/:loc_id/details
        PATCH /locations/:loc_id/details

        Query Parameters
        Parameter	Validations	Required	Description
        id	        Integer	    true	    The id of the location.
        timezone	String	    false	    The location timezone.
        currency	String	    false	    The location accepted currency
        description	String	    false	    The location description
        food_served	String	    false	    The food served at the location
        growler_filling_station	String	false	Whether the location fills growlers
        crowler_filling_station	String	false	Whether the location fills crowlers
        kegs	    String	    false	Whether the location carries kegs
        nitro_on_tap	String	false	Whether the location has nitro on tap
        cask_on_tap	String	false	Whether the location has casks on tap
        serve_wine	String	false	Whether the location serves wine
        serve_liquor	String	false	Whether the location serves liquor
        serve_cocktails	String	false	Whether the location serves cocktails
        categories	String[]	false	The location categories
        accepted_payment_types	String[]	false	The location accepted payment types

        e.g. { "currency": "USD", "description": "We really like beer here!",
               "nitro_on_tap": 1, "categories": ["55a59bace4b013909087cb36"] }

        :param loc_id:
        :param loc_data:
        :return:
        """
        pass



    def list_ufb_items(self):
        """
        locations->menus->sections->items
        :return:
        """
        pass

    def track_ufb_event(self):
        """
        https://docs.business.untappd.com/#events
        GET locations/:location_id/analytics
        :return:
        """
        pass

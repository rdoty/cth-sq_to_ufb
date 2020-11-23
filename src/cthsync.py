import requests

from base64 import b64encode
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

    def update_square_location(self):
        location = settings.get("square", {}).get("main_loc_id")
        location_data = settings.get("square", {}).get("location_data")
        result = self.square_client.locations.update_location(location, location_data)
        return result.body if result.is_success() else f"Error: {result.errors}"

    def list_ufb_locations(self):
        ufb = requests.get(self.ufb_api + "locations", headers=self.ufb_headers)
        return ufb.json() if ufb.status_code == 200 else ufb.status_code

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

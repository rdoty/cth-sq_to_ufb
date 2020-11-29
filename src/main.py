from pprint import pprint

from settings import *

from cthsync import CTHSync


def main():
    """
    UFB API Documentation
    https://docs.business.untappd.com/#introduction

    SquareUp Python SDK Documentation
    https://github.com/square/square-python-sdk/blob/master/doc/client.md
    """
    cth = CTHSync()

    print("Square locations:")
    square_locations = cth.get_square_locations()
    pprint(square_locations)

    print("Square inventory counts:")
    inventory_counts = cth.get_square_inventory_counts()
    pprint(inventory_counts)

    print("UFB locations:")
    location_data = cth.get_ufb_locations()
    pprint(location_data)
    pprint(location_data[0]["id"])

    # TODO Update Stripe location data with UFB location information
    locations = settings.get("square", {}).get("locations")
    # print("Updating location settings:")
    # for location in locations:
    #     for location_id, location_data in location.items():
    #         pprint(cth.update_square_location(location_id, location_data))

    print("UFB announcements:")
    announcements = cth.get_ufb_loc_info("social_announcements")
    pprint(announcements)

    print("UFB menus:")
    menus = cth.get_ufb_loc_info("menus")
    for menu in menus:
        print(menu)

    sizes = cth.get_ufb_container_sizes()
    print(f"Count of UFB container sizes: {len(sizes['container_sizes'])}")


if __name__ == "__main__":
    main()

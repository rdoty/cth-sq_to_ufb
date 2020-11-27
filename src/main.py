from pprint import pprint

from settings import *

from cthsync import CTHSync


def main():
    """
    UFB API Documentation
    https://docs.business.untappd.com/#introduction

    SquareUp Python SDK Documentation
    https://github.com/square/square-python-sdk/tree/master/doc/api
    """
    cth = CTHSync()

    print("Square locations:")
    pprint(cth.list_square_locations())

    locations = settings.get("square", {}).get("locations")
    # print("Updating location settings:")
    # for location in locations:
    #     for location_id, location_data in location.items():
    #         pprint(cth.update_square_location(location_id, location_data))

    print("Square inventory counts:")
    pprint(cth.list_square_inventory_counts())

    print("UFB locations:")
    pprint(cth.list_ufb_locations())

    print("UFB list_ufb_container_sizes:")
    sizes = cth.list_ufb_container_sizes()
    count = 0
    for size in sizes['container_sizes']:
        count += 1
        print(f"{count} - '{size.get('name')}' ")


if __name__ == "__main__":
    main()

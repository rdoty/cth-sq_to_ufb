from pprint import pprint

from cthsync import CTHSync


def main():
    """
    UFB API Documentation
    https://docs.business.untappd.com/#introduction

    SquareUp Python SDK Documentation
    https://github.com/square/square-python-sdk/blob/master/doc/client.md
    """
    cth = CTHSync()

    square_location = cth.get_square_locations()[0]
    print(f"\nSquare first location ID: {square_location['id']}")

    ufb_location = cth.get_ufb_locations()[0]
    print(f"\nUFB first location ID: {ufb_location['id']}")

    # TODO Update square_location with info from ufb_location
    # for location in ufb_location:
    #     for location_id, location_data in location.items():
    #         pprint(cth.update_square_location(location_id, location_data))

    print("\nSquare inventory counts:")
    inventory_counts = cth.get_square_inventory_counts()
    pprint(inventory_counts)

    print("\nSquare item catalogs:")
    for catalog_type in cth.square_valid_catalog_types:
        catalog = cth.get_square_catalog(catalog_type)
        pprint(f"{catalog_type}: {catalog}")

    print("\nUFB announcements:")
    announcements = cth.get_ufb_loc_info("social_announcements")
    pprint(announcements)

    print("\nUFB menu descriptions:")
    menus = cth.get_ufb_loc_info("menus")
    for menu in menus:
        print(menu["description"])

    sizes = cth.get_ufb_container_sizes()
    print(f"\nCount of UFB container sizes: {len(sizes['container_sizes'])}")


if __name__ == "__main__":
    main()

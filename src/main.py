from pprint import pprint

from cthsync import CTHSync


def main():
    """
    UFB API Documenation
    https://docs.business.untappd.com/#introduction

    SquareUp Python SDK Documentation
    https://github.com/square/square-python-sdk/tree/master/doc/api
    """
    cth = CTHSync()

    pprint(cth.list_square_locations())
    # Update server with current values in settings.py and display
    # pprint(f"Updated location settings:\n {cth.update_square_location()}")

    pprint(f"Square inventory counts:\n {cth.list_square_inventory_counts()}")
    pprint(f"UFB inventory counts:\n {cth.list_ufb_locations()}")


if __name__ == "__main__":
    main()

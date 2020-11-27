import json

with open("secure.json", "r") as secure_file:
    secure_settings = json.load(secure_file)

settings = {
    "square": {
        "locations": [
            {
                "H5WXDNE10ZYJJ": {
                    "location": {
                        "address": {
                            "address_line_1": "3513 Clayton Rd",
                            "administrative_district_level_1": "CA",
                            "locality": "Concord",
                            "postal_code": "94519-2421",
                        },
                        "business_hours": {
                            "periods": [
                                {
                                    "day_of_week": "MON",
                                    "end_local_time": "17:00",
                                    "start_local_time": "09:00",
                                }
                            ]
                        },
                        "description": "Concord Tap House",
                        "facebook_url": "https://www.facebook.com/concordtaphouse",
                        "instagram_username": "concordtaphouse",
                        "name": "Concord Tap House",
                        "twitter_username": "concordtaphouse",
                    },
                },
            },
        ]
    },
    "ufb": {
        "location_id": "15939",
        "api_root": "https://business.untappd.com/api/v1/",
    },
}

import os
import json

# CITY INFO
CITY_ID = 'a92c434a-7050-49bd-aaea-4b0eafd63448'

# RATING INFO
RATING_MIN = '100'
RATING_MAX = '10000'

# PRICING INFO
PRICE = '0'
PRICE_PER_HOUR = '1900'
PRICE_PERCENTAGE =  '0'
FEE = '2090'
FEE_PER_HOUR = '100'
FEE_PERCENTAGE = '0'

# DISTRICT INFO
DISTRICTS_LIST_PATH = 'bairros-floripa.txt'
OUTPUT_JSON_PATH = 'districts_floripa.json'

def load_display_names(districts_list_path):
    file = open(districts_list_path, 'r')
    display_names = file.read().split('\n')

    return display_names


def export_districts_json(path, districts_json):
    file = open(path, 'w')
    file.write(districts_json)
    file.close()


def district_json(display_name):
    district_js = {
        "data": {
            "type": "districts",
            "attributes": {
                "display_name": display_name,
                "code": district_code(display_name),
                "active": "true"
            },
            "relationships": {
                "city": city_json(),
                "rating": rating_json(),
                "pricing": pricing_json()
            }
        }
    }

    return district_js


def districts_json(display_names_list):
    districts_list = []

    for display_name in display_names_list:
        districts_list.append(district_json(display_name))
    
    return districts_list


def pricing_json():
    pricing_js = {
        "attributes": {
            "price": PRICE,
            "price_per_hour": PRICE_PER_HOUR,
            "price_percentage": PRICE_PERCENTAGE,
            "fee": FEE,
            "fee_per_hour": FEE_PER_HOUR,
            "fee_percentage": FEE_PERCENTAGE
        }
    }

    return pricing_js


def rating_json():
    rating_js = {
        "attributes": {
            "rating_min": RATING_MIN,
            "rating_max": RATING_MAX
        }
    }

    return rating_js


def city_json():
    city_js = {
        "attributes": {
            "id": CITY_ID
        }
    }

    return city_js


def district_code(display_name):
    words = display_name.split()
    words_count = len(words)

    if words_count == 1:
        return display_name[0:3].upper()
    elif words_count == 2:
        return ''.join(word[0] for word in words).upper() + words[1][1].upper()
    elif words_count >= 3:
        return ''.join(word[0] for word in words).upper()[0:3]


display_names_list = load_display_names(DISTRICTS_LIST_PATH)
districts_json_list = districts_json(display_names_list)
export_districts_json(OUTPUT_JSON_PATH, json.dumps(districts_json_list, indent=4, ensure_ascii=False))

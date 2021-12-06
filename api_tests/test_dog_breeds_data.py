import requests


def get_list_of_all_breeds():
    res = requests.get("https://dog.ceo/api/breeds/list/all")
    breeds_json = res.json().get("message")
    return breeds_json


all_breeds_list = get_list_of_all_breeds()


def get_list_of_breeds_and_sub_breeds():
    for breed in all_breeds_list.items():
        for sub_breed in breed[1]:
            # return breed and sub-breed
            yield breed[0], sub_breed

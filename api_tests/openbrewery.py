import pytest
import requests

base_url = "https://api.openbrewerydb.org/breweries"


@pytest.mark.parametrize("city", ['Portland', 'Denver', 'San Diego'])
def test_array_of_breweries_by_city(city):
    res = requests.get(url=base_url, params={'by_city': city})
    assert res.status_code == 200
    for i in res.json():
        assert i["city"] == city


@pytest.mark.parametrize("state, sorting_field",
                         [('Minnesota', 'city'),
                          ('Ohio', 'city'),
                          ('New Mexico', 'id')
                          ])
def test_array_of_breweries_by_state_sorting(state, sorting_field):
    res = requests.get(url=base_url, params={'by_state': state, 'sort': f'{sorting_field}:asc'})
    assert res.status_code == 200
    list_of_values = []
    for i in res.json():
        assert i["state"] == state
        list_of_values.append(i[sorting_field])
    assert list_of_values == sorted(list_of_values)


@pytest.mark.parametrize("postal_code", ['46534', '89502', '44107'])
def test_array_of_breweries_by_postal_code(postal_code):
    res = requests.get(url=base_url, params={'by_postal': postal_code})
    assert res.status_code == 200
    for i in res.json():
        assert i["postal_code"].startswith(postal_code)


@pytest.mark.parametrize("items_per_page", [0, 1, 20, 33, 50])
def test_array_of_breweries_items_per_page(items_per_page):
    res = requests.get(url=base_url, params={'per_page': items_per_page})
    assert res.status_code == 200
    assert len(res.json()) == items_per_page


@pytest.mark.parametrize("items_per_page", [-1, "word"])
def test_array_of_breweries_per_page_wrong_value(items_per_page):
    res = requests.get(url=base_url, params={'per_page': items_per_page})
    assert res.status_code == 200
    assert len(res.json()) == 20


@pytest.mark.parametrize("search_term", ["Dog", "Ale"])
def test_get_list_of_ids_names_based_on_search_term(search_term):
    target = base_url + "/autocomplete"
    res = requests.get(url=target, params={'query': search_term})
    assert res.status_code == 200
    for i in res.json():
        assert search_term in i["name"]

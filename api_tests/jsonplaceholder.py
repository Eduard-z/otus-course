import random
import requests
import pytest
from jsonschema import validate

base_url = "https://jsonplaceholder.typicode.com"


def test_get_all_albums():
    target = base_url + "/albums"
    res = requests.get(url=target)
    assert res.status_code == 200
    assert len(res.json()) == 100


@pytest.mark.parametrize("album_id", [1, 33, 100])
def test_get_album_by_id(album_id):
    target = base_url + "/albums/{}".format(album_id)
    res = requests.get(url=target)
    assert res.status_code == 200
    assert res.json().get("id") == album_id


@pytest.mark.parametrize("user_id", [1, 10])
def test_filtering_album_by_user_id(user_id):
    target = base_url + "/albums"
    res = requests.get(url=target, params={'userId': user_id})
    random_post_number = random.randint(0, 9)
    assert res.status_code == 200
    assert res.json()[random_post_number]["userId"] == user_id


@pytest.mark.parametrize("post_id", [-1, 0, 101, 'a'])
def test_filtering_comments_by_post_id_wrong_value(post_id):
    target = base_url + "/comments"
    res = requests.get(url=target, params={'postId': post_id})
    assert res.status_code == 200
    assert res.json() == []


@pytest.mark.parametrize("input_title, output_title",
                         [('title1', 'title1'),
                          ('', ''),
                          (111, '111'),
                          ('&', '&')
                          ])
@pytest.mark.parametrize("post_body", ['foo', 222])
@pytest.mark.parametrize("user_id", [1, 10])
def test_create_post(input_title, output_title, post_body, user_id):
    target = base_url + "/posts"
    res = requests.post(url=target, data={'title': input_title, 'body': post_body, 'userId': user_id})
    res_json = res.json()
    assert res.status_code == 201
    assert res_json.get("title") == output_title
    assert res_json.get("body") == str(post_body)
    assert res_json.get("userId") == str(user_id)


@pytest.mark.parametrize("input_title, output_title",
                         [('title1', 'title1'),
                          ('', ''),
                          (111, '111'),
                          ('&', '&')
                          ])
@pytest.mark.parametrize("post_body", ['foo', 222])
@pytest.mark.parametrize("user_id, post_id",
                         [(1, 1),
                          (10, 99)])
def test_update_post(input_title, output_title, post_body, user_id, post_id):
    target = base_url + f"/posts/{post_id}"
    res = requests.put(url=target,
                       data={'title': input_title, 'body': post_body, 'userId': user_id, 'id': post_id}
                       )
    res_json = res.json()
    assert res.status_code == 200
    assert res_json.get("title") == output_title
    assert res_json.get("body") == str(post_body)
    assert res_json.get("userId") == str(user_id)


@pytest.mark.parametrize("input_title, output_title",
                         [('title1', 'title1'),
                          ('', ''),
                          (111, '111'),
                          ('&', '&')
                          ])
@pytest.mark.parametrize("user_id, post_id",
                         [(1, 1),
                          (3, 22)])
def test_patch_post(input_title, output_title, user_id, post_id):
    target = base_url + f"/posts/{post_id}"
    res = requests.patch(url=target, data={'title': input_title})
    res_json = res.json()
    assert res.status_code == 200
    assert res_json.get("title") == output_title
    assert res_json.get("userId") == user_id


@pytest.mark.parametrize("user_id, post_id", [(1, 1), (4, 33)])
def test_delete_post_by_id(user_id, post_id):
    target = base_url + f"/posts/{post_id}"
    res = requests.delete(url=target)
    assert res.status_code == 200


@pytest.mark.parametrize("post_id", [1, 33])
def test_api_json_schema_post_by_id(post_id):
    target = base_url + f"/posts/{post_id}"
    res = requests.get(url=target)

    schema = {"type": "object",
              "properties": {
                  "id": {"type": "number"},
                  "userId": {"type": "number"},
                  "title": {"type": "string"},
                  "body": {"type": "string"}
              },
              "required": ["id", "userId", "title", "body"]
              }

    validate(instance=res.json(), schema=schema)

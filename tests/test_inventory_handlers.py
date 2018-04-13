import json
import os
from uuid import uuid4

import requests

from fixture import (
    ITEM_COLLECTION,
    ITEM_DETAIL,
    ITEM_TYPE_COLLECTION,
    LOCAL_HOST
)


def make_request(method, url, payload=None):
    path = os.path.join(LOCAL_HOST, url)
    if method == 'post':
        return requests.post(url=path, json=payload)
    else:
        return requests.get(path)


def test_get_item_types():
    response = make_request('get', ITEM_TYPE_COLLECTION)
    assert response.status_code == 200

    data = json.loads(response.text)
    assert ['Book', 'Comic', 'Movie', 'Music', 'Video_Game'] == data


def test_post_no_payload():
    response = make_request('post', ITEM_COLLECTION)
    assert response.status_code == 400


def test_post_non_existent_type():
    payload = {
        'title': 'test title {uuid}'.format(uuid=uuid4()),
        'itemType': 'butts'
    }

    response = make_request('post', ITEM_COLLECTION, payload)

    assert response.status_code == 404


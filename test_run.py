import json

from run import app


def test_healthcheck():
    request, response = app.test_client.get(
        '/api/v1/healthcheck'
    )

    assert response.status == 200
    assert 'healty' in response.json


def test_user():
    request, response = app.test_client.post(
        '/api/v1/users',
        data=json.dumps({
            'username': 'ismetacar'
        })
    )

    assert response.status == 400
    assert response.json['error'] == 'badRequest'

    request, response = app.test_client.post(
        '/api/v1/users',
        data=json.dumps({
            'username': 'ismetacar',
            'password': '123123'
        })
    )

    assert response.status == 200
    assert response.json['username'] == 'ismetacar'


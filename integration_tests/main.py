import requests


BASE_URL = "http://web:8000"


def _request(method, endpoint, data=None):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.request(method, url, json=data)
    return response


def test_create_cart():
    response = _request("POST", "carts", {"total_amount": "5.50"})
    assert response.status_code == 201
    assert response.json()["cart_uuid"] is not None


def test_create_cart_with_invalid_total_amount():
    response = _request("POST", "carts", {"total_amount": "invalid"})
    assert response.status_code == 422


def test_get_all_carts():
    _request("POST", "carts", {"total_amount": "5.50"})
    response = _request("GET", "carts")
    assert response.status_code == 200
    assert len(response.json()["carts"]) > 0


def test_get_cart_by_uuid_not_found():
    response = _request("GET", "carts/invalid")
    assert response.status_code == 404


def test_get_cart_by_uuid():
    response = _request("POST", "carts", {"total_amount": "5.50"})
    cart_uuid = response.json()["cart_uuid"]
    response = _request("GET", f"carts/{cart_uuid}")
    assert response.status_code == 200
    assert response.json()["uuid"] == cart_uuid


def test_update_cart_not_found():
    response = _request("PUT", "carts/invalid")
    assert response.status_code == 404


def test_update_cart():
    response = _request("POST", "carts", {"total_amount": "5.50"})
    cart_uuid = response.json()["cart_uuid"]
    response = _request("PUT", f"carts/{cart_uuid}", {"total_amount": "10.50"})
    assert response.status_code == 200
    response = _request("GET", f"carts/{cart_uuid}")
    assert response.json()["total_amount"] == 10.50


def test_delete_cart_not_found():
    response = _request("DELETE", "carts/invalid")
    assert response.status_code == 404


def test_delete_cart():
    response = _request("POST", "carts", {"total_amount": "5.50"})
    cart_uuid = response.json()["cart_uuid"]
    response = _request("DELETE", f"carts/{cart_uuid}")
    assert response.status_code == 200
    response = _request("GET", f"carts/{cart_uuid}")
    assert response.status_code == 404

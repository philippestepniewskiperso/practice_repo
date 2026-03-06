def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_items_empty(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item(client):
    response = client.post("/items", json={"name": "apple"})
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["name"] == "apple"


def test_create_item_increments_id(client):
    first = client.post("/items", json={"name": "apple"}).json()
    second = client.post("/items", json={"name": "banana"}).json()
    assert second["id"] == first["id"] + 1


def test_create_item_missing_name(client):
    response = client.post("/items", json={})
    assert response.status_code == 422


def test_get_item(client):
    created = client.post("/items", json={"name": "apple"}).json()
    response = client.get(f"/items/{created['id']}")
    assert response.status_code == 200
    assert response.json() == created


def test_get_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_list_items_after_create(client):
    client.post("/items", json={"name": "apple"})
    client.post("/items", json={"name": "banana"})
    response = client.get("/items")
    assert response.status_code == 200
    names = [item["name"] for item in response.json()]
    assert names == ["apple", "banana"]

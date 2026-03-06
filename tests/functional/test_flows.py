def test_create_and_retrieve_item(client):
    """Creating an item makes it retrievable by id."""
    created = client.post("/items", json={"name": "apple"}).json()
    fetched = client.get(f"/items/{created['id']}").json()
    assert fetched["name"] == created["name"]


def test_create_multiple_items_and_list(client):
    """All created items appear in the listing."""
    names = ["apple", "banana", "cherry"]
    created_ids = [client.post("/items", json={"name": n}).json()["id"] for n in names]

    items = client.get("/items").json()
    listed_ids = [item["id"] for item in items]
    assert created_ids == listed_ids


def test_items_are_isolated_between_tests(client):
    """Store is empty at the start of every test (relies on reset_store fixture)."""
    response = client.get("/items")
    assert response.json() == []


def test_id_sequence_restarts_after_reset(client):
    """After store reset, ids start from 1 again."""
    item = client.post("/items", json={"name": "apple"}).json()
    assert item["id"] == 1

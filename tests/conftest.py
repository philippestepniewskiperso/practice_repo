import pytest
from starlette.testclient import TestClient

import practicerepo.app as app_module
from practicerepo.app import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_store():
    """Reset the in-memory store before each test."""
    app_module._items.clear()
    app_module._next_id = 1

import pytest
from pydantic import ValidationError

from practicerepo.models import Item, ItemCreate


def test_item_create_valid():
    item = ItemCreate(name="apple")
    assert item.name == "apple"


def test_item_create_missing_name():
    with pytest.raises(ValidationError):
        ItemCreate()


def test_item_create_rejects_non_string():
    # Pydantic coerces ints to strings in lax mode, but None should fail
    with pytest.raises(ValidationError):
        ItemCreate(name=None)


def test_item_valid():
    item = Item(id=1, name="apple")
    assert item.id == 1
    assert item.name == "apple"


def test_item_missing_fields():
    with pytest.raises(ValidationError):
        Item(id=1)

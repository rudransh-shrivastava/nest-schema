"""Test cases for the sponsor schema validation."""

import pytest

from tests.conftest import common_negative_test, common_positive_test

SCHEMA_NAME = "sponsor"


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        ("description_empty.yaml", "$.description: '' is too short"),
        ("description_null.yaml", "$.description: None is not of type 'string'"),
        ("logo_empty.yaml", "$.logo: '' is not a 'uri'"),
        ("logo_null.yaml", "$.logo: None is not a 'uri'"),
        ("name_empty.yaml", "$.name: '' is too short"),
        ("name_null.yaml", "$.name: None is not of type 'string'"),
        ("name_undefined.yaml", "$: 'name' is a required property"),
        ("url_empty.yaml", "$.url: '' is not a 'uri'"),
        ("url_null.yaml", "$.url: None is not a 'uri'"),
        ("url_undefined.yaml", "$: 'url' is a required property"),
    ],
)
def test_negative(common_schema, file_path, error_message):
    """Test invalid cases for the sponsor schema."""
    common_negative_test(common_schema, SCHEMA_NAME, file_path, error_message)


def test_positive(common_schema):
    """Test valid cases for the sponsor schema."""
    common_positive_test(common_schema, SCHEMA_NAME)

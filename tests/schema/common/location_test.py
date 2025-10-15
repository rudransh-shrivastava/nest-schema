"""Test cases for the location schema validation."""

import pytest

from tests.conftest import common_negative_test, common_positive_test

SCHEMA_NAME = "location"


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        ("address_empty.yaml", "$.address: '' is too short"),
        ("address_null.yaml", "$.address: None is not of type 'string'"),
        ("city_empty.yaml", "$.city: '' is too short"),
        ("city_null.yaml", "$.city: None is not of type 'string'"),
        ("country_empty.yaml", "$.country: '' is too short"),
        ("country_null.yaml", "$.country: None is not of type 'string'"),
        ("country_undefined.yaml", "$: 'country' is a required property"),
        ("country_code_empty.yaml", "$.country_code: '' does not match '^[A-Z]{2}$'"),
        ("country_code_invalid.yaml", "$.country_code: 'USA' does not match '^[A-Z]{2}$'"),
        ("country_code_null.yaml", "$.country_code: None is not of type 'string'"),
        ("country_code_undefined.yaml", "$: 'country_code' is a required property"),
        ("latitude_invalid_high.yaml", "$.latitude: 91 is greater than the maximum of 90"),
        ("latitude_invalid_low.yaml", "$.latitude: -91 is less than the minimum of -90"),
        ("latitude_null.yaml", "$.latitude: None is not of type 'number'"),
        ("latitude_string.yaml", "$.latitude: '40.7128' is not of type 'number'"),
        ("longitude_invalid_high.yaml", "$.longitude: 181 is greater than the maximum of 180"),
        ("longitude_invalid_low.yaml", "$.longitude: -181 is less than the minimum of -180"),
        ("longitude_null.yaml", "$.longitude: None is not of type 'number'"),
        ("longitude_string.yaml", "$.longitude: '-74.0060' is not of type 'number'"),
        ("postal_code_empty.yaml", "$.postal_code: '' is too short"),
        ("postal_code_null.yaml", "$.postal_code: None is not of type 'string'"),
        ("region_empty.yaml", "$.region: '' is too short"),
        ("region_null.yaml", "$.region: None is not of type 'string'"),
        ("timezone_empty.yaml", "$.timezone: '' is too short"),
        ("timezone_null.yaml", "$.timezone: None is not of type 'string'"),
    ],
)
def test_negative(common_schema, file_path, error_message):
    """Test invalid cases for the location schema."""
    common_negative_test(common_schema, SCHEMA_NAME, file_path, error_message)


def test_positive(common_schema):
    """Test valid cases for the location schema."""
    common_positive_test(common_schema, SCHEMA_NAME)

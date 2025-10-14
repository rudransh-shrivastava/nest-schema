"""Test cases for the mailing list schema validation."""

import pytest

from tests.conftest import common_negative_test, common_positive_test

SCHEMA_NAME = "mailing_list"


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        ("description_empty.yaml", "$.description: '' is too short"),
        ("description_null.yaml", "$.description: None is not of type 'string'"),
        ("email_empty.yaml", "$.email: '' is not a 'email'"),
        ("email_null.yaml", "$.email: None is not a 'email'"),
        ("title_empty.yaml", "$.title: '' is too short"),
        ("title_null.yaml", "$.title: None is not of type 'string'"),
        ("url_empty.yaml", "$.url: '' is not a 'uri'"),
        ("url_invalid.yaml", "$.url: 'https://xyz' is not a 'uri'"),
        ("url_null.yaml", "$.url: None is not a 'uri'"),
    ],
)
def test_negative(common_schema, file_path, error_message):
    """Test invalid mailing list schema cases."""
    common_negative_test(common_schema, SCHEMA_NAME, file_path, error_message)


def test_positive(common_schema):
    """Test valid mailing list schema cases."""
    common_positive_test(common_schema, SCHEMA_NAME)

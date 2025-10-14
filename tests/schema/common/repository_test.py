"""Test cases for the repository schema validation."""

import pytest

from tests.conftest import common_negative_test, common_positive_test

SCHEMA_NAME = "repository"


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        ("changelog_empty.yaml", "$.changelog: '' is not a 'uri'"),
        ("changelog_null.yaml", "$.changelog: None is not a 'uri'"),
        ("code_of_conduct_empty.yaml", "$.code_of_conduct: '' is not a 'uri'"),
        ("code_of_conduct_null.yaml", "$.code_of_conduct: None is not a 'uri'"),
        ("contribution_guide_empty.yaml", "$.contribution_guide: '' is not a 'uri'"),
        ("contribution_guide_null.yaml", "$.contribution_guide: None is not a 'uri'"),
        ("description_empty.yaml", "$.description: '' is too short"),
        ("description_null.yaml", "$.description: None is not of type 'string'"),
        ("invalid_name.yaml", "$.name: 'xy' is too short"),
        ("name_empty.yaml", "$.name: '' is too short"),
        ("name_null.yaml", "$.name: None is not of type 'string'"),
        ("url_empty.yaml", "$.url: '' is not a 'uri'"),
        ("url_invalid.yaml", "$.url: 'github/repo' is not a 'uri'"),
        ("url_null.yaml", "$.url: None is not a 'uri'"),
        ("url_undefined.yaml", "$: 'url' is a required property"),
    ],
)
def test_negative(common_schema, file_path, error_message):
    """Test invalid cases for the repository schema."""
    common_negative_test(common_schema, SCHEMA_NAME, file_path, error_message)


def test_positive(common_schema):
    """Test valid cases for the repository schema."""
    common_positive_test(common_schema, SCHEMA_NAME)

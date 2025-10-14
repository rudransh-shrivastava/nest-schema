"""Committee schema tests."""

from pathlib import Path

import pytest
import yaml

from owasp_schema.utils.schema_validators import validate_data
from tests.conftest import tests_data_dir


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        ("community_empty.yaml", "$.community: [] should be non-empty"),
        (
            "community_non_unique.yaml",
            "$.community: [{'platform': 'discord', 'url': 'https://discord.com/example'}, "
            "{'platform': 'discord', 'url': 'https://discord.com/example'}] "
            "has non-unique elements",
        ),
        ("community_null.yaml", "$.community: None is not of type 'array'"),
        ("description_null.yaml", "$.description: None is not of type 'string'"),
        ("events_empty.yaml", "$.events: [] should be non-empty"),
        (
            "events_non_unique.yaml",
            "$.events: [{'url': 'https://example.com/event1'}, "
            "{'url': 'https://example.com/event1'}] has non-unique elements",
        ),
        ("events_null.yaml", "$.events: None is not of type 'array'"),
        ("mailing_list_empty.yaml", "$.mailing_list: [] should be non-empty"),
        ("mailing_list_null.yaml", "$.mailing_list: None is not of type 'array'"),
        ("members_empty.yaml", "$.members: [] is too short"),
        ("members_null.yaml", "$.members: None is not of type 'array'"),
        ("members_undefined.yaml", "$: 'members' is a required property"),
        ("logo_empty.yaml", "$.logo: [] should be non-empty"),
        ("logo_null.yaml", "$.logo: None is not of type 'array'"),
        (
            "logo_non_unique.yaml",
            "$.logo: [{'small': 'https://example.com/smallLogo.png', "
            "'medium': 'https://example.com/mediumLogo.png', "
            "'large': 'https://example.com/largeLogo.png'}, "
            "{'small': 'https://example.com/smallLogo.png', "
            "'medium': 'https://example.com/mediumLogo.png', "
            "'large': 'https://example.com/largeLogo.png'}] has non-unique elements",
        ),
        ("meeting_minutes_null.yaml", "$.meeting_minutes: None is not of type 'array'"),
        ("meeting_minutes_invalid.yaml", "$.meeting_minutes[0].url: 'https://xyz' is not a 'uri'"),
        ("name_empty.yaml", "$.name: '' is too short"),
        ("name_null.yaml", "$.name: None is not of type 'string'"),
        ("name_undefined.yaml", "$: 'name' is a required property"),
        ("resources_invalid.yaml", "$.resources[0].url: 'https://xyz' is not a 'uri'"),
        ("resources_null.yaml", "$.resources: None is not of type 'array'"),
        ("scope_null.yaml", "$.scope: None is not of type 'string'"),
        ("scope_invalid.yaml", "$: 'scope' is a required property"),
        ("social_media_empty.yaml", "$.social_media: [] should be non-empty"),
        ("social_media_invalid.yaml", "$.social_media[0].url: 'https://xyz' is not a 'uri'"),
        ("social_media_null.yaml", "$.social_media: None is not of type 'array'"),
        ("sponsors_empty.yaml", "$.sponsors: [] should be non-empty"),
        ("sponsors_invalid.yaml", "$.sponsors[0].url: 'https://xyz' is not a 'uri'"),
        ("sponsors_null.yaml", "$.sponsors: None is not of type 'array'"),
        ("tags_empty.yaml", "$.tags: [] is too short"),
        ("tags_null.yaml", "$.tags: None is not of type 'array'"),
        ("tags_undefined.yaml", "$: 'tags' is a required property"),
        ("website_empty.yaml", "$.website: '' is not a 'uri'"),
        ("website_null.yaml", "$.website: None is not a 'uri'"),
    ],
)
def test_negative(committee_schema, file_path, error_message):
    assert (
        validate_data(
            committee_schema,
            yaml.safe_load(
                Path(tests_data_dir / "schema/committee/negative" / file_path).read_text(),
            ),
        )
        == error_message
    )


def test_positive(committee_schema):
    for file_path in Path(tests_data_dir / "schema/committee/positive").rglob("*.yaml"):
        assert (
            validate_data(
                committee_schema,
                yaml.safe_load(
                    file_path.read_text(),
                ),
            )
            is None
        )

"""This module tests config.py."""

from typing import Dict
import pytest
from alias_cd import config


@pytest.fixture
def config_data() -> str:
    """Sample config data in yaml format."""

    return """---
  "~":
    _alias: root

    my_long_directory_1:
      _alias: d1

      my_sub_directory_1:
        _alias: sd1

      my_sub_directory_2:
        my_sub_directory_3:
          _alias: sd3"""


@pytest.fixture
def config_yaml() -> Dict:
    """Sample config data as a dictonary."""

    return {
        "~": {
            "_alias": "root",
            "my_long_directory_1": {
                "_alias": "d1",
                "my_sub_directory_1": {"_alias": "sd1"},
                "my_sub_directory_2": {"my_sub_directory_3": {"_alias": "sd3"}},
            },
        },
    }


@pytest.fixture
def config_obj() -> config.Config:
    """Sample config data as a Config object."""

    return config.Config(
        aliases={
            "root": "~",
            "d1": "~/my_long_directory_1",
            "sd1": "~/my_long_directory_1/my_sub_directory_1",
            "sd3": "~/my_long_directory_1/my_sub_directory_2/my_sub_directory_3",
        },
    )


def test_yaml_parsing(config_data, config_yaml):
    """Test that the config_data fixture matches the config_yaml fixture."""

    assert config._load_yaml(config_data) == config_yaml


def test_config_parsing(config_yaml, config_obj):
    """Test that the _get_config creates the Config object correctly."""

    assert config._get_config(config_yaml=config_yaml) == config_obj

from typing import Dict
import pytest
from alias_cd import config


@pytest.fixture
def config_data() -> str:

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
def config_yaml(config_data) -> Dict:
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
    return config.Config(
        aliases={
            "root": "~",
            "d1": "~/my_long_directory_1",
            "sd1": "~/my_long_directory_1/my_sub_directory_1",
            "sd3": "~/my_long_directory_1/my_sub_directory_2/my_sub_directory_3",
        },
    )


def test_yaml_parsing(config_data, config_yaml):
    assert config._load_yaml(config_data) == config_yaml


def test_config_parsing(config_yaml, config_obj):

    assert config._get_config(config_yaml=config_yaml) == config_obj

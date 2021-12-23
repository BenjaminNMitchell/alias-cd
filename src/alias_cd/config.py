"""This module contains the configuration parsing logic."""

from dataclasses import dataclass
from typing import Dict
import os

import yaml


ALIAS_KEY = "_alias"
DEFAULT_CONFIG_PATH = os.path.join(
    os.path.expanduser("~"), ".config", "alias_cd", "config.yaml"
)


@dataclass
class Config:
    aliases: Dict[str, str]


def _load_config(config_path: str = None):
    """Parse the configuration file from the supplied"""

    if config_path is None:
        config_path = DEFAULT_CONFIG_PATH

    if not os.path.exists(config_path):
        raise ValueError(f"No config file found at {config_path}")

    with open(config_path, "r") as stream:
        config_yaml = _load_yaml(stream)

    return _get_config(config_yaml)


def _get_config(config_yaml: Dict) -> Config:

    return Config(aliases=_get_aliases(config_yaml))


def _load_yaml(data):
    return yaml.safe_load(data)


def _get_aliases(config_yaml: Dict, base_path="") -> Config:
    """Depth first search for aliases"""

    aliases = {}

    if ALIAS_KEY in config_yaml:
        aliases[config_yaml["_alias"]] = base_path

    for key, value in config_yaml.items():
        if key != ALIAS_KEY:
            aliases.update(_get_aliases(value, base_path=os.path.join(base_path, key)))

    return aliases

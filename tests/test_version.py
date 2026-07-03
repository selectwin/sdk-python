from importlib.metadata import version as _dist_version

import selectwin
from selectwin import SDK_VERSION


def test_sdk_version_derives_from_installed_metadata():
    # SDK_VERSION must come from the package metadata (single source of truth =
    # pyproject.toml), never a hardcoded constant that drifts on release.
    assert SDK_VERSION == _dist_version("selectwin")


def test_dunder_version_matches():
    assert selectwin.__version__ == SDK_VERSION

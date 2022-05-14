"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("plexmediaserver"),
    ],
)
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


def test_plexmediaserver_running_and_enabled(host):
    servicename = host.service("plexmediaserver")
    assert servicename.is_running
    assert servicename.is_enabled

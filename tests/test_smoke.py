"""Basic package import smoke test."""


def test_package_version_is_available() -> None:
    import machinelearning2

    assert machinelearning2.__version__

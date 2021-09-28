"""
A pytest plugin to skip `@pytest.mark.slow` tests by default. 
Include the slow tests with `--slow`.
"""

__version__ = '0.0.2'

import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")

def pytest_addoption(parser):
    parser.addoption("--slow", action="store_true",
                     default=False,
                     help="include tests marked slow")

def pytest_collection_modifyitems(config, items):
    if not config.getoption("--slow"):
        skip_slow = pytest.mark.skip(reason="need --slow option to run")
        for item in items:
            if item.get_closest_marker("slow"):
                item.add_marker(skip_slow)


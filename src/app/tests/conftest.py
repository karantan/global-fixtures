"""Various specific py.test fixtures.

Usually we want to have here:

* Reading test.ini settings

* Setting up and tearing down database

* Creating a WSGI application to test

* Spinning up a WSGI server for functional test run
"""
from _pytest.config import main

import logging
import pytest
import os

logger = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def dbsession(request):
    """Create dict that represents database and database session."""
    database = {'value': 'App value'}

    return database


def pytest_collection_modifyitems(config, items):
    """Collect framework tests."""
    import framework

    framework_dir = os.path.join(framework.__path__[0], 'tests')
    exitcode = main([
        framework_dir,
        '--confcutdir={}'.format(os.path.dirname(__file__)),
    ])
    if exitcode != 0:
        raise Exception('Framework browser test failed!')

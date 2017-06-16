"""Various specific py.test fixtures.

Usually we want to have here:

* Reading test.ini settings

* Setting up and tearing down database

* Creating a WSGI application to test

* Spinning up a WSGI server for functional test run
"""
import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def dbsession(request, autouse=True):
    """Create dict that represents database and database session."""
    database = {'value': 'App value'}

    return database

from __future__ import absolute_import, unicode_literals

import pytest

from advancescholar.users.models import User
from advancescholar.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()

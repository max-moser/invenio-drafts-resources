# SPDX-FileCopyrightText: 2020-2021 CERN.
# SPDX-FileCopyrightText: 2020-2025 Northwestern University.
# SPDX-License-Identifier: MIT

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

import pytest
from mock_module.api import Draft
from mock_module.service import (
    MediaFilesRecordServiceConfig,
    ServiceConfig,
)

from invenio_drafts_resources.services.records import RecordService


@pytest.fixture(scope="module")
def service():
    """Service instance."""
    return RecordService(ServiceConfig)


@pytest.fixture(scope="module")
def service_with_media_files(media_file_service, media_draft_file_service):
    """Service instance."""
    return RecordService(
        MediaFilesRecordServiceConfig,
        files_service=media_file_service,
        draft_files_service=media_draft_file_service,
    )


@pytest.fixture()
def example_record(app, db):
    """Example record."""
    record = Draft.create({}, metadata={"title": "Test"})
    db.session.commit()
    return record


@pytest.fixture()
def app(app, location):
    """Auto-use location fixture."""
    return app

# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-FileCopyrightText: 2025 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Module tests."""

from datetime import datetime

import pytest
from invenio_indexer.api import RecordIndexer
from mock_module.api import Draft


@pytest.fixture()
def example_draft(db, input_data, location):
    """Example draft."""
    draft = Draft.create(input_data, expires_at=datetime(2020, 9, 7, 0, 0))
    draft.commit()
    db.session.commit()
    return draft


@pytest.fixture()
def indexer():
    """Indexer instance with correct Record class."""
    return RecordIndexer(record_cls=Draft, record_to_index=lambda r: r.index._name)

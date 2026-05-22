# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Northwestern University.
# SPDX-License-Identifier: MIT

"""Test utilities."""


def create_and_publish(service, identity_simple, input_data):
    """Creates a draft and publishes it."""
    draft = service.create(identity_simple, input_data)
    record = service.publish(identity_simple, draft.id)

    assert record.id == draft.id
    assert record._record.revision_id == 2

    return record

# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Northwestern University.
# SPDX-FileCopyrightText: 2022 Graz University of Technology.
# SPDX-License-Identifier: MIT


from .utils import create_and_publish


def create_two_versions(service, identity_simple, input_data):
    """Create 2 versions."""
    record = create_and_publish(service, identity_simple, input_data)
    draft = service.new_version(identity_simple, record.id)
    # new_version resets files.enabled to True
    service.update_draft(identity_simple, draft.id, input_data)
    record_2 = service.publish(identity_simple, draft.id)
    service.record_cls.index.refresh()
    return [record, record_2]


def test_search_versions(app, identity_simple, input_data, service):
    v1, v2 = create_two_versions(service, identity_simple, input_data)

    # test search defaults to latest version
    results = service.search(identity_simple)
    assert set([v2.id]) == set([r["id"] for r in results])

    # test search all versions
    results = service.search(identity_simple, params={"allversions": True})
    assert set([v1.id, v2.id]) == set([r["id"] for r in results])


def test_search_versions_for_record(app, identity_simple, input_data, service):
    v1, v2 = create_two_versions(service, identity_simple, input_data)

    # test search_versions defaults to all versions
    results = service.search_versions(identity_simple, v2.id)
    assert set([v1.id, v2.id]) == set([r["id"] for r in results])

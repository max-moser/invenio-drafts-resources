# SPDX-FileCopyrightText: 2020-2021 CERN.
# SPDX-FileCopyrightText: 2020-2021 Northwestern University.
# SPDX-License-Identifier: MIT

"""Test draft service links."""

from copy import deepcopy


def assert_expected_links(pid_value, links):
    expected_links = {
        "self": f"https://127.0.0.1:5000/api/mocks/{pid_value}/draft",
        "publish": f"https://127.0.0.1:5000/api/mocks/{pid_value}/draft/actions/publish",  # noqa
    }

    for key, link in expected_links.items():
        assert link == links[key]


def test_create_draft(client, headers, input_data, location):
    response = client.post("/mocks", json=input_data, headers=headers)

    assert response.status_code == 201
    pid_value = response.json["id"]
    assert_expected_links(pid_value, response.json["links"])


def test_read_draft(client, headers, input_data, location):
    response = client.post("/mocks", json=input_data, headers=headers)
    pid_value = response.json["id"]
    response = client.get(f"/mocks/{pid_value}/draft", headers=headers)

    assert response.status_code == 200
    assert_expected_links(pid_value, response.json["links"])


def test_update_draft(client, headers, input_data, location):
    response = client.post("/mocks", json=input_data, headers=headers)
    pid_value = response.json["id"]
    input_data = deepcopy(input_data)
    input_data["metadata"]["title"] = "Updated title"  # Shouldn't matter

    response = client.put(f"/mocks/{pid_value}/draft", json=input_data, headers=headers)

    assert response.status_code == 200
    assert_expected_links(pid_value, response.json["links"])


def test_publish_draft(client, headers, input_data, location):
    response = client.post("/mocks", json=input_data, headers=headers)
    pid_value = response.json["id"]

    # NOTE: This returns a record
    response = client.post(f"/mocks/{pid_value}/draft/actions/publish", headers=headers)

    assert response.status_code == 202
    links = response.json["links"]
    expected_links = {
        "self": f"https://127.0.0.1:5000/api/mocks/{pid_value}",
        # TODO: Add files, delete...
    }
    for key, link in expected_links.items():
        assert link == links[key]

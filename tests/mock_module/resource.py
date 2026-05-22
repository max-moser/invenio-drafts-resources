# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-FileCopyrightText: 2025 Northwestern University.
# SPDX-License-Identifier: MIT

"""Example resource."""

from invenio_records_resources.resources import (
    FileResource,
)
from invenio_records_resources.resources import (
    FileResourceConfig as FileResourceConfigBase,
)

from invenio_drafts_resources.resources import RecordResource, RecordResourceConfig

from .service import (
    draft_file_service,
    file_service,
    record_service,
)


# Config
class RecordResourceConfig(RecordResourceConfig):
    """Mock record resource configuration."""

    blueprint_name = "mocks"
    url_prefix = "/mocks"


class FileResourceConfig(FileResourceConfigBase):
    """Mock record file resource."""

    blueprint_name = "mocks_files"
    url_prefix = "/mocks/<pid_value>"


class DraftFileResourceConfig(FileResourceConfigBase):
    """Mock record file resource."""

    blueprint_name = "mocks_draft_files"
    url_prefix = "/mocks/<pid_value>/draft"


# Resources
resource_for_mocks_draft_files = FileResource(
    DraftFileResourceConfig,
    draft_file_service,
)
resource_for_mocks_files = FileResource(FileResourceConfig, file_service)
resource_for_mocks_records = RecordResource(RecordResourceConfig, record_service)

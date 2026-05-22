# SPDX-FileCopyrightText: 2023 CERN.
# SPDX-License-Identifier: MIT

"""Records service component base classes."""

from invenio_records_resources.services.base.config import _make_cls
from invenio_records_resources.services.records.components.files import FilesAttrConfig

from .base import BaseRecordFilesComponent

# Configure file attributes for files component
DraftFilesComponent = _make_cls(BaseRecordFilesComponent, {**FilesAttrConfig})

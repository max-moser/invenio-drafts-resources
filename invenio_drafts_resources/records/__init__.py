# SPDX-FileCopyrightText: 2020-2021 CERN.
# SPDX-FileCopyrightText: 2021 Northwestern University.
# SPDX-License-Identifier: MIT

"""Data layer API.

The 'records' folder name stands for the generic records-resource's data layer.
It applies to both api.py's Draft and Record.
"""

from .api import Draft, ParentRecord, Record
from .models import DraftMetadataBase, ParentRecordMixin, ParentRecordStateMixin

__all__ = (
    "Draft",
    "DraftMetadataBase",
    "ParentRecord",
    "ParentRecordMixin",
    "ParentRecordStateMixin",
    "Record",
)

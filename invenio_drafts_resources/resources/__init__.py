# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-FileCopyrightText: 2020 Northwestern University.
# SPDX-License-Identifier: MIT

"""REST APIs for working with records, drafts and files."""

from .records import RecordResource, RecordResourceConfig

__all__ = (
    "RecordResource",
    "RecordResourceConfig",
)

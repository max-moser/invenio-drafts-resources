# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-FileCopyrightText: 2020 Northwestern University.
# SPDX-License-Identifier: MIT

"""Override of RecordResources."""

from .config import RecordResourceConfig
from .resource import RecordResource

__all__ = (
    "RecordResource",
    "RecordResourceConfig",
)

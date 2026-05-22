# SPDX-FileCopyrightText: 2020-2021 CERN.
# SPDX-FileCopyrightText: 2021 Northwestern University.
# SPDX-License-Identifier: MIT

"""Record service component for drafts."""

from .base import ServiceComponent
from .files import DraftFilesComponent
from .media_files import DraftMediaFilesComponent
from .metadata import DraftMetadataComponent
from .pid import PIDComponent
from .relations import RelationsComponent

__all__ = (
    "ServiceComponent",
    "DraftFilesComponent",
    "DraftMetadataComponent",
    "PIDComponent",
    "RelationsComponent",
    "DraftMediaFilesComponent",
)

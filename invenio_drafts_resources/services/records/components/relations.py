# SPDX-FileCopyrightText: 2021-2025 CERN.
# SPDX-License-Identifier: MIT

"""Records service relations component."""

from invenio_records_resources.services.records.components import (
    RelationsComponent as RelationsComponentBase,
)


class RelationsComponent(RelationsComponentBase):
    """Relations service component."""

    def read_draft(self, identity, draft=None, errors=None):
        """Read draft handler."""
        draft.relations.dereference()

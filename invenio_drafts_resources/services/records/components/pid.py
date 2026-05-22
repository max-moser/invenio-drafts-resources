# SPDX-FileCopyrightText: 2020-2021 CERN.
# SPDX-FileCopyrightText: 2021 Northwestern University.
# SPDX-FileCopyrightText: 2023 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Records service component base classes."""

from invenio_records_resources.services.records.components import ServiceComponent


class PIDComponent(ServiceComponent):
    """Service component for PID registraion."""

    def publish(self, identity, draft=None, record=None):
        """Register persistent identifiers when publishing."""
        if not record.is_published:
            record.register()

    def delete_draft(self, identity, draft=None, record=None, force=False):
        """Unregister persistent identifiers for unpublished drafts."""
        if force:
            draft.__class__.pid.session_merge(draft)
            draft.pid.delete()

            # Only delete parent PID if there are no other versions
            if draft.versions.latest_index == 1:
                draft.parent.__class__.pid.session_merge(draft.parent)
                draft.parent.pid.delete()

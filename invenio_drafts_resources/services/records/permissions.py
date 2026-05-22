# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-FileCopyrightText: 2020 Northwestern University.
# SPDX-License-Identifier: MIT

"""Drafts permissions."""

from invenio_records_permissions.generators import AnyUser
from invenio_records_permissions.policies.records import (
    RecordPermissionPolicy as RecordPermissionPolicyBase,
)


class RecordPermissionPolicy(RecordPermissionPolicyBase):
    """Custom permission policy."""

    # FIXME: Revist this along the development
    # Default create should be "authenticated"?
    # TODO: Subclass records-resources policy and add *_draft actions
    can_create = [AnyUser()]
    can_new_version = [AnyUser()]
    can_edit = [AnyUser()]
    can_publish = [AnyUser()]
    can_read_draft = [AnyUser()]
    can_update_draft = [AnyUser()]
    can_delete_draft = [AnyUser()]
    can_manage_files = [AnyUser()]

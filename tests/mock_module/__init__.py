# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-FileCopyrightText: 2025 Northwestern University.
# SPDX-License-Identifier: MIT

"""Mock test module."""

from .resource import (
    resource_for_mocks_draft_files,
    resource_for_mocks_files,
    resource_for_mocks_records,
)
from .service import (
    draft_file_service,
    file_service,
)


# Blueprints
def create_bp_of_mocks_records(app):
    """Create mocks API Blueprint."""
    return resource_for_mocks_records.as_blueprint()


def create_bp_of_mocks_draft_files(app):
    """Create mocks API Blueprint."""
    return resource_for_mocks_draft_files.as_blueprint()


def create_bp_of_mocks_files(app):
    """Create mocks API Blueprint."""
    return resource_for_mocks_files.as_blueprint()


# Finalize
def finalize_app(app):
    """Init app."""
    # Register services - cannot be done in extension because
    # Invenio-Records-Resources might not have been initialized.
    registry = app.extensions["invenio-records-resources"].registry
    registry.register(file_service, service_id="service-for-mocks-files")
    registry.register(draft_file_service, service_id="service-for-mocks-draft-files")

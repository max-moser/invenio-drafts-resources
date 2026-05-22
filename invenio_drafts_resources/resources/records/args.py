# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Northwestern University.
# SPDX-License-Identifier: MIT

"""Schemas for parameter parsing."""

from invenio_records_resources.resources.records.args import (
    SearchRequestArgsSchema as SearchRequestArgsSchemaBase,
)
from marshmallow import fields


class SearchRequestArgsSchema(SearchRequestArgsSchemaBase):
    """Extend schema with all versions field."""

    allversions = fields.Boolean()
    include_deleted = fields.Boolean()

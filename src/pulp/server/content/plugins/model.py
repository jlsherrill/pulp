# -*- coding: utf-8 -*-
#
# Copyright © 2011 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

"""
This module contains transfer objects for encapsulating data passed into a
plugin method call. Objects defined in this module will have extra information
bundled in that is relevant to the plugin's state for the given entity.
"""

class Repository:
    """
    Contains repository data and any additional data relevant for the plugin to
    function.

    @ivar id: programmatic ID for the repository
    @type id: str

    @ivar display_name: user-friendly name describing the repository
    @type display_name: str or None

    @ivar description: user-friendly description of the repository
    @type description: str or None

    @ivar notes: arbitrary key-value pairs set and used by users to
                 programmatically describe the repository
    @type notes: str or None

    @ivar working_dir: local (to the Pulp server) directory the importer may use
          to store any temporary data required by the importer; this directory
          is unique for each repository
    @type working_dir: str
    """

    def __init__(self, id, display_name=None, description=None, notes=None):
        self.id = id
        self.display_name = display_name
        self.description = description
        self.notes = notes

        self.working_dir = None

    def __str__(self):
        return 'Repository [%s]' % self.id
        
class Unit:
    """
    Contains information related to a single content unit. The unit may or
    may not exist in Pulp; this is meant simply as a way of linking together
    a number of pieces of data.

    @ivar id: Pulp internal ID that refers to this unit; if the unit does not
              yet exist in Pulp, this will be None
    @type id: str

    @ivar unit_key: natural key for the content unit
    @type unit_key: dict

    @ivar type_id: ID of the unit's type
    @type type_id: str

    @ivar metadata: mapping of key/value pairs describing the unit
    @type metadata: dict

    @ivar storage_path: full path to where on disk the unit is stored
    @type storage_path: str
    """

    def __init__(self, type_id, unit_key, metadata, storage_path):
        self.type_id = type_id
        self.unit_key = unit_key
        self.metadata = metadata
        self.storage_path = storage_path

        self.id = None

    def __str__(self):
        return 'Unit [key=%s] [type=%s] [id=%s]' % (self.unit_key, self.type_id, self.id)

class SyncReport:
    """
    Returned to the Pulp server at the end of a sync call. This is used by the
    plugin to describe what took place during the sync.

    @ivar added_count: number of new units added during the sync
    @type added_count: int

    @ivar updated_count: number of units updated during the sync
    @type updated_count: int

    @ivar removed_count: number of units unassociated from the repo during the sync
    @type removed_count: int

    @ivar summary: arbitrary value that will be returned by default as the log
                   for the sync (should be short)
    @type summary: just about any serializable object (likely str or dict)

    @ivar details: potentially longer log that will have to be specifically
                   retrieved through the Pulp REST APIs
    @type details: just about any serializable object (likley str or dict)
    """

    def __init__(self, added_count, updated_count, removed_count, summary, details):
        self.added_count = added_count
        self.updated_count = updated_count
        self.removed_count = removed_count
        self.summary = summary
        self.details = details

class PublishReport:
    """
    Returned to the Pulp server at the end of a publish call. This is used by the
    plugin to decrive what took place during the publish run.

    @ivar summary: arbitrary value that will be returned by default as the log
                   for the call (should be short)
    @type summary: just about any serializable object (likely str or dict)

    @ivar details: potentially longer log that will have to be specifically
                   retrieved through the Pulp REST APIs
    @type details: just about any serializable object (likley str or dict)
    """

    def __init__(self, summary, details):
        self.summary = summary
        self.details = details
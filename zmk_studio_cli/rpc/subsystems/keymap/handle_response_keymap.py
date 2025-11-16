# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""keymap Response handler"""

from ....logger import log_dbg
from ....proto import keymap_pb2 as keymap
from .error_conditions import (
    ERR_SAVE_CHANGES,
    RESP_SET_LAYER_BINDING,
)


def handle_response_get_keymap(response: keymap.Response):
    """Print keymap"""
    stored_keymap = response.get_keymap
    log_dbg("keymap", stored_keymap)


def handle_response_set_layer_binding(response: keymap.Response):
    """Print set layer binding response"""
    set_layer_binding_resp = response.set_layer_binding
    log_dbg("keymap", "Set layer binding:")
    log_dbg("keymap", RESP_SET_LAYER_BINDING[set_layer_binding_resp])


def handle_response_check_unsaved_changes(response: keymap.Response):
    """Print unsaved changes status"""
    unsaved_changes = response.check_unsaved_changes
    log_dbg("keymap", f"Check unsaved changes: {unsaved_changes}")


def handle_response_save_changes(response: keymap.Response):
    """Print saved changes status"""
    saved_changes_err = response.save_changes.err
    log_dbg("keymap", f"Save changes: {ERR_SAVE_CHANGES[saved_changes_err]}")


def handle_response_discard_changes(response: keymap.Response):
    """Print discard changes status"""
    discard_changes = response.discard_changes
    log_dbg("keymap", f"Discarded changes? {discard_changes}")

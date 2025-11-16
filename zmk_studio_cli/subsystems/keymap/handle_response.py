# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""keymap Response handler"""

from ...proto import keymap_pb2 as keymap
from .handle_response_keymap import (
    handle_response_get_keymap,
    handle_response_set_layer_binding,
    handle_response_check_unsaved_changes,
    handle_response_save_changes,
    handle_response_discard_changes,
)
from .handle_response_physical_layouts import (
    handle_response_get_physical_layouts,
    handle_response_set_active_physical_layout,
)
from .handle_response_layers import (
    handle_response_move_layer,
    handle_response_add_layer,
    handle_response_remove_layer,
    handle_response_restore_layer,
    handle_response_set_layer_props,
)


def handle_response(response: keymap.Response):
    """Handle keymap Response from ZMK Studio RPC Protocol"""

    response_type = response.WhichOneof("response_type")
    if response_type == "get_keymap":
        handle_response_get_keymap(response=response)

    if response_type == "set_layer_binding":
        handle_response_set_layer_binding(response=response)

    if response_type == "check_unsaved_changes":
        handle_response_check_unsaved_changes(response=response)

    if response_type == "save_changes":
        handle_response_save_changes(response=response)

    if response_type == "discard_changes":
        handle_response_discard_changes(response=response)

    if response_type == "get_physical_layouts":
        handle_response_get_physical_layouts(response=response)

    if response_type == "set_active_physical_layout":
        handle_response_set_active_physical_layout(response=response)

    if response_type == "move_layer":
        handle_response_move_layer(response=response)

    if response_type == "add_layer":
        handle_response_add_layer(response=response)

    if response_type == "remove_layer":
        handle_response_remove_layer(response=response)

    if response_type == "restore_layer":
        handle_response_restore_layer(response=response)

    if response_type == "set_layer_props":
        handle_response_set_layer_props(response=response)

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""keymap Response handler"""

from ...proto import keymap_pb2 as keymap
from .error_conditions import ERR_SET_ACTIVE_PHYSICAL_LAYOUT
from ...logger import log_dbg, log_err


def handle_response_get_physical_layouts(response: keymap.Response):
    """Print physical layouts"""
    physical_layouts = response.get_physical_layouts
    log_dbg("keymap", physical_layouts)


def handle_response_set_active_physical_layout(response: keymap.Reponse):
    """Print set active physical layout error code"""
    resp_err = response.set_active_physical_layout.err
    log_dbg("keymap", "Set active physical layout:")
    if resp_err == 0:
        log_dbg("keymap", "Layout set.")
    else:
        log_err("keymap", ERR_SET_ACTIVE_PHYSICAL_LAYOUT[resp_err])

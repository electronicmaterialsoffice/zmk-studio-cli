# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""keymap Response handler"""

from ....logger import log_dbg, log_err
from ....proto import keymap_pb2 as keymap
from .error_conditions import (
    ERR_ADD_LAYER,
    ERR_MOVE_LAYER,
    ERR_REMOVE_LAYER,
    ERR_RESTORE_LAYER,
    RESP_SET_LAYER_PROPS,
)


def handle_response_move_layer(response: keymap.Response):
    """Print move layer error code"""
    resp_err = response.move_layer.err
    if resp_err == 0:
        log_dbg("keymap", "Layer moved.")
    else:
        log_err("keymap", ERR_MOVE_LAYER[resp_err])


def handle_response_add_layer(response: keymap.Response):
    """Print add layer error code"""
    resp_err = response.add_layer.err
    if resp_err == 0:
        log_dbg("keymap", "Layer added.")
    else:
        log_err("keymap", ERR_ADD_LAYER[resp_err])


def handle_response_remove_layer(response: keymap.Response):
    """Print remove layer error code"""
    resp_err = response.remove_layer.err
    if resp_err == 0:
        log_dbg("keymap", "SUCCESS")
    else:
        log_err("keymap", ERR_REMOVE_LAYER[resp_err])


def handle_response_restore_layer(response: keymap.Response):
    """Print restore layer error code"""
    resp_err = response.restore_layer.err
    if resp_err == 0:
        log_dbg("keymap", "SUCCESS")
    else:
        log_err("keymap", ERR_RESTORE_LAYER[resp_err])


def handle_response_set_layer_props(response: keymap.Response):
    """Print set layer properties error code"""
    resp_err = response.set_layer_props.err
    if resp_err == 0:
        log_dbg("keymap", "SUCCESS")
    else:
        log_err("keymap", RESP_SET_LAYER_PROPS[resp_err])


def handle_response_layer_active(response: keymap.Response):
    """Print layer active state at chosen layer ID"""
    log_dbg("keymap", f"Layer active: {response.layer_active}")


def handle_response_layer_locked(response: keymap.Response):
    """Print layer lock state at chosen layer ID"""
    log_dbg("keymap", f"Layer locked: {response.layer_locked}")


def handle_response_layer_activate(response: keymap.Response):
    """Print layer activate response at chosen layer ID"""
    log_dbg("keymap", f"Layer activate: {response.layer_activate}")


def handle_response_layer_deactivate(response: keymap.Response):
    """Print layer deactivate response at chosen layer ID"""
    log_dbg("keymap", f"Layer deactivate: {response.layer_deactivate}")


def handle_response_layer_toggle(response: keymap.Response):
    """Print layer toggle response at chosen layer ID"""
    log_dbg("keymap", f"Layer toggle: {response.layer_toggle}")


def handle_response_layer_to(response: keymap.Response):
    """Print layer to response at chosen layer ID"""
    log_dbg("keymap", f"Layer to: {response.layer_to}")

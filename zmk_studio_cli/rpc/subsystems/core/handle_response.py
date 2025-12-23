# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""core Response handler"""

from ....logger import log_dbg
from ....proto import core_pb2 as core
from .lockstate import LOCKSTATE


def handle_response(response: core.Response):
    """Handle core Response from ZMK Studio RPC Protocol"""
    response_type = response.WhichOneof("response_type")
    if response_type == "get_device_info":
        handle_response_get_device_info(response=response)
    if response_type == "get_lock_state":
        handle_response_get_lock_state(response=response)
    if response_type == "reset_settings":
        handle_response_reset_settings(response=response)
    if response_type == "save_changes":
        handle_response_save_changes(response=response)
    if response_type == "discard_changes":
        handle_response_discard_changes(response=response)
    if response_type == "check_unsaved_changes":
        handle_response_check_unsaved_changes(response=response)


def handle_response_get_device_info(response: core.Response):
    """Print device info"""
    device_info = response.get_device_info
    log_dbg("core", f"Device Name: {device_info.name}")
    log_dbg("core", f"   Serial #: {device_info.serial_number}")


def handle_response_get_lock_state(response: core.Response):
    """Print lock state"""
    lock_state = response.get_lock_state
    log_dbg("core", f"Lock state: {LOCKSTATE[lock_state]}")


def handle_response_reset_settings(response: core.Response):
    """Print reset settings status"""
    log_dbg("core", f"Reset settings: {response.reset_settings}")


def handle_response_save_changes(response: core.Response):
    """Print check unsaved changes"""
    res = response.save_changes
    log_dbg("core", f"saved changes? {res}")


def handle_response_discard_changes(response: core.Response):
    """Print discard changes result"""
    res = response.discard_changes
    log_dbg("core", f"discard changes? {res}")


def handle_response_check_unsaved_changes(response: core.Response):
    """Print check unsaved changes"""
    unsaved = response.check_unsaved_changes
    log_dbg("core", f"Unsaved changes? {unsaved}")

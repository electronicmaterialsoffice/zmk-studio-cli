# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
ZMK Studio RPC Protocol functions
"""

import google.protobuf
import serial

from .logger import log_dbg, log_err, log_notif
from .proto import studio_pb2 as studio
from .subsytems import behaviors, core, keymap, meta

RPC_SOF = b"\xab"
RPC_ESC = b"\xac"
RPC_EOF = b"\xad"


def send_request(ser: serial.Serial, request: bytes):
    """Send Request message via ZMK Studio RPC Protocol"""
    ser.write(RPC_SOF)
    ser.write(request.SerializeToString())
    ser.write(RPC_EOF)


def get_response(ser: serial.Serial, verbose: bool):
    """Get Response mesage from ZMK Studio RPC Protocol"""
    response_msg = b""
    response_chr = ser.read()
    if response_chr == RPC_SOF:
        while True:
            response_chr = ser.read()
            if response_chr == RPC_ESC:
                response_chr = ser.read()
                response_msg = response_msg + response_chr
                continue
            if response_chr == RPC_EOF:
                break
            response_msg = response_msg + response_chr
    if verbose is True:
        print(response_msg)
    return response_msg


def handle_response(response_msg: bytes):
    """Handle Response message from ZMK Studio RPC Protocol"""
    response = studio.Response()
    try:
        response.ParseFromString(response_msg)
    except google.protobuf.message.DecodeError:
        log_err("", "Could not parse incoming response.")
        return

    response_type = response.WhichOneof("type")

    if response_type == "request_response":
        req_response = response.request_response
        handle_request_response(req_response)

    if response_type == "notification":
        notification = response.notification
        handle_notification(notification)


def handle_request_response(request_response: studio.RequestResponse):
    """Handle RequestResponse from ZMK Studio RPC Protocol"""
    req_response_subsystem = request_response.WhichOneof("subsystem")

    if req_response_subsystem == "meta":
        handle_response_meta(request_response.meta)
    if req_response_subsystem == "core":
        handle_response_core(request_response.core)
    if req_response_subsystem == "behaviors":
        handle_response_behaviors(request_response.behaviors)
    if req_response_subsystem == "keymap":
        handle_response_keymap(request_response.keymap)


def handle_response_meta(request_response_meta: any):
    """Handle meta Response from ZMK Studio RPC Protocol"""
    response_type = request_response_meta.WhichOneof("response_type")
    if response_type == "no_response":
        return
    if response_type == "simple_error":
        simple_error_index = request_response_meta.simple_error
        log_err("meta", meta.ERROR_CONDITIONS[simple_error_index])


def handle_response_core(request_response_core: any):
    """Handle core Response from ZMK Studio RPC Protocol"""
    response_type = request_response_core.WhichOneof("response_type")
    if response_type == "get_device_info":
        device_info = request_response_core.get_device_info
        log_dbg("core", f"Device Name: {device_info.name}")
        log_dbg("core", f"   Serial #: {device_info.serial_number}")
    if response_type == "get_lock_state":
        lock_state = request_response_core.get_lock_state
        log_dbg("core", f"Lock state: {core.LOCKSTATE[lock_state]}")
    if response_type == "reset_settings":
        log_dbg("core", f"Reset settings: {request_response_core.reset_settings}")


def handle_response_behaviors(request_response_behaviors: any):
    """Handle behaviors Response from ZMK Studio RPC Protocol"""
    behaviors_response_type = request_response_behaviors.WhichOneof("response_type")
    if behaviors_response_type == "list_all_behaviors":
        log_dbg("behaviors", "Listing all behaviors...")
        log_dbg("behaviors", request_response_behaviors.list_all_behaviors.behaviors)
    if behaviors_response_type == "get_behavior_details":
        behavior_id = request_response_behaviors.get_behavior_details.id
        behavior_display_name = (
            request_response_behaviors.get_behavior_details.display_name
        )
        behavior_metadata = request_response_behaviors.get_behavior_details.metadata
        log_dbg("behaviors", f"Behavior ID: {behavior_id}")
        log_dbg("behaviors", f"Display Name: {behavior_display_name}")
        if len(behavior_metadata) > 0:
            log_dbg("behaviors", "Metadata:\n", behavior_metadata)


def handle_response_keymap(request_response_keymap: any):
    """Handle keymap Response from ZMK Studio RPC Protocol"""

    def log_dbg_keymap(*args, **kwargs):
        log_dbg("keymap", *args, **kwargs)

    def log_err_keymap(*args, **kwargs):
        log_err("keymap", *args, **kwargs)

    keymap_response_type = request_response_keymap.WhichOneof("response_type")
    if keymap_response_type == "get_keymap":
        stored_keymap = request_response_keymap.get_keymap
        log_dbg_keymap(stored_keymap)
    if keymap_response_type == "set_layer_binding":
        set_layer_binding_resp = request_response_keymap.set_layer_binding
        log_dbg_keymap("Set layer binding:")
        log_dbg_keymap(keymap.RESP_SET_LAYER_BINDING[set_layer_binding_resp])
    if keymap_response_type == "check_unsaved_changes":
        unsaved_changes = request_response_keymap.check_unsaved_changes
        log_dbg_keymap(f"Check unsaved changes: {unsaved_changes}")
    if keymap_response_type == "save_changes":
        saved_changes_err = request_response_keymap.save_changes.err
        log_dbg_keymap(f"Save changes: {keymap.ERR_SAVE_CHANGES[saved_changes_err]}")
    if keymap_response_type == "discard_changes":
        discard_changes = request_response_keymap.discard_changes
        log_dbg_keymap(f"Discarded changes? {discard_changes}")
    if keymap_response_type == "get_physical_layouts":
        physical_layouts = request_response_keymap.get_physical_layouts
        log_dbg_keymap(physical_layouts)
    if keymap_response_type == "set_active_physical_layout":
        resp_err = request_response_keymap.set_active_physical_layout.err
        log_dbg_keymap("Set active physical layout:")
        if resp_err == 0:
            log_dbg_keymap("Layout set.")
        else:
            log_err_keymap(keymap.ERR_SET_ACTIVE_PHYSICAL_LAYOUT[resp_err])
    if keymap_response_type == "move_layer":
        resp_err = request_response_keymap.move_layer.err
        if resp_err == 0:
            log_dbg_keymap("Layer moved.")
        else:
            log_err_keymap(keymap.ERR_MOVE_LAYER[resp_err])
    if keymap_response_type == "add_layer":
        resp_err = request_response_keymap.add_layer.err
        if resp_err == 0:
            log_dbg_keymap("Layer added.")
        else:
            log_err_keymap(keymap.ERR_ADD_LAYER[resp_err])
    if keymap_response_type == "remove_layer":
        resp_err = request_response_keymap.remove_layer.err
        if resp_err == 0:
            log_dbg_keymap("SUCCESS")
        else:
            log_err_keymap(keymap.ERR_REMOVE_LAYER[resp_err])
    if keymap_response_type == "restore_layer":
        resp_err = request_response_keymap.restore_layer.err
        if resp_err == 0:
            log_dbg_keymap("SUCCESS")
        else:
            log_err_keymap(keymap.ERR_RESTORE_LAYER[resp_err])
    if keymap_response_type == "set_layer_props":
        resp_err = request_response_keymap.set_layer_props.err
        if resp_err == 0:
            log_dbg_keymap("SUCCESS")
        else:
            log_err_keymap(keymap.RESP_SET_LAYER_PROPS[resp_err])


def handle_notification(notification: studio.Notification):
    """Handle Notification message from ZMK Studio RPC Protocol"""
    notification_subsystem = notification.WhichOneof("subsystem")

    if notification_subsystem == "core":
        core_notification_type = notification.core.WhichOneof("notification_type")
        if core_notification_type == "lock_state_changed":
            lock_state = notification.core.lock_state_changed
            log_notif("core", f"LOCK STATE: {core.LOCKSTATE[lock_state]}")
            return
        print("<err> Invalid notification type")
        return

    if notification_subsystem == "keymap":
        keymap_notification_type = notification.keymap.WhichOneof("notification_type")
        if keymap_notification_type == "unsaved_changes_status_changed":
            unsaved_changes_status_changed = (
                notification.keymap.unsaved_changes_status_changed
            )
            log_notif(
                "keymap",
                "Unsaved changes status changed:",
                unsaved_changes_status_changed,
            )
            return
        print("<err> Invalid notification type")
        return

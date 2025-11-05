# Copyright (c) 2025 Electronic Materials Office Ltd.
# SPDX-License-Identifier: MIT
"""
ZMK Studio RPC Protocol functions
"""

import serial
from .proto import studio_pb2 as studio
from . import errors

RPC_SOF = b"\xab"
RPC_ESC = b"\xac"
RPC_EOF = b"\xad"


def send_request(ser: serial.Serial, request: bytes):
    """Send Request message via ZMK Studio RPC Protocol"""
    ser.write(RPC_SOF)
    ser.write(request.SerializeToString())
    ser.write(RPC_EOF)


def get_response(ser: serial.Serial, verbose: bool):
    """Handle Response mesage from ZMK Studio RPC Protocol"""
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
    response = studio.Response()
    try:
        response.ParseFromString(response_msg)
    except Exception as error:
        print("An exception occurred: ", error)
        return

    response_type = response.WhichOneof("type")

    if response_type == "request_response":
        req_response = response.request_response
        handle_request_response(req_response)

    if response_type == "notification":
        notification = response.notification
        handle_notification(notification)


def handle_request_response(request_response: any):
    """Handle RequestResponse from ZMK Studio RPC Protocol"""
    req_response_subsystem = request_response.WhichOneof("subsystem")

    if req_response_subsystem == "meta":
        meta_response_type = request_response.meta.WhichOneof("response_type")
        if meta_response_type == "no_response":
            print("<meta> NO RESPONSE")
        if meta_response_type == "simple_error":
            simple_error_index = request_response.meta.simple_error
            print(f"<meta> SIMPLE ERROR: {errors.ERRORCONDITIONS[simple_error_index]}")
    if req_response_subsystem == "core":
        core_response_type = request_response.core.WhichOneof("response_type")
        if core_response_type == "get_device_info":
            device_info = request_response.core.get_device_info
            print(f"<core> Device Name: {device_info.name}")
            print(f"<core>    Serial #: {device_info.serial_number}")
        if core_response_type == "get_lock_state":
            lock_state = request_response.core.get_lock_state
            print(f"<core> LOCK STATE: {errors.LOCKSTATE[lock_state]}")
        if core_response_type == "reset_settings":
            print(f"<core> Reset settings: {request_response.core.reset_settings}")

    if req_response_subsystem == "behaviors":
        behaviors_response_type = request_response.behaviors.WhichOneof("response_type")
        if behaviors_response_type == "list_all_behaviors":
            print("<behaviors> Listing all behaviors...")
            print(request_response.behaviors.list_all_behaviors.behaviors)
        if behaviors_response_type == "get_behavior_details":
            behavior_id = request_response.behaviors.get_behavior_details.id
            behavior_display_name = (
                request_response.behaviors.get_behavior_details.display_name
            )
            behavior_metadata = request_response.behaviors.get_behavior_details.metadata
            print(f"<behaviors> Behavior ID: {behavior_id}")
            print(f"<behaviors> Display Name: {behavior_display_name}")
            if len(behavior_metadata) > 0:
                print("<behaviors> Metadata:")
                print(behavior_metadata)

    if req_response_subsystem == "keymap":
        keymap_response_type = request_response.keymap.WhichOneof("response_type")
        if keymap_response_type == "get_keymap":
            keymap = request_response.keymap.get_keymap
            print(keymap)
        if keymap_response_type == "set_layer_binding":
            set_layer_binding_resp = request_response.keymap.set_layer_binding
            print("<keymap> Set layer binding:")
            print(errors.SETLAYERBINDINGRESPONSE[set_layer_binding_resp])
        if keymap_response_type == "check_unsaved_changes":
            unsaved_changes = request_response.keymap.check_unsaved_changes
            print(f"<keymap> Check unsaved changes: {unsaved_changes}")
        if keymap_response_type == "save_changes":
            saved_changes_ok = request_response.keymap.save_changes.ok
            saved_changes_err = request_response.keymap.save_changes.err
            print(f"<keymap> Saved changes? {saved_changes_ok}")
            if saved_changes_err:
                print("<keymap> Saved changes err:")
                print(errors.SAVECHANGESERRORCODE[saved_changes_err])
        if keymap_response_type == "discard_changes":
            discard_changes = request_response.keymap.discard_changes
            print(f"<keymap> Discarded changes? {discard_changes}")
        if keymap_response_type == "get_physical_layouts":
            physical_layouts = request_response.keymap.get_physical_layouts
            print(physical_layouts)
        if keymap_response_type == "set_active_physical_layout":
            resp_err = request_response.keymap.set_active_physical_layout.err
            print("<keymap> Set active physical layout:")
            print(errors.SETACTIVEPHYSICALLAYOUTERRORCODE[resp_err])
        if keymap_response_type == "move_layer":
            resp_err = request_response.keymap.move_layer.err
            print(f"<keymap> Move layer: {errors.MOVELAYERERRORCODE[resp_err]}")
        if keymap_response_type == "add_layer":
            resp_err = request_response.keymap.add_layer.err
            print(f"<keymap> Add layer: {errors.ADDLAYERERRORCODE[resp_err]}")
        if keymap_response_type == "remove_layer":
            resp_err = request_response.keymap.remove_layer.err
            print(f"<keymap> Remove layer: {errors.REMOVELAYERERRORCODE[resp_err]}")
        if keymap_response_type == "restore_layer":
            resp_err = request_response.keymap.restore_layer.err
            print(f"<keymap> Restore layer: {errors.ADDLAYERERRORCODE[resp_err]}")
        if keymap_response_type == "set_layer_props":
            resp_err = request_response.keymap.set_layer_props.err
            print(f"<keymap> Set layer props: {errors.SETLAYERPROPSRESPONSE[resp_err]}")


def handle_notification(notification: any):
    """Handle Notification message from ZMK Studio RPC Protocol"""
    notification_subsystem = notification.WhichOneof("subsystem")

    if notification_subsystem == "core":
        core_notification_type = notification.core.WhichOneof("notification_type")
        if core_notification_type == "lock_state_changed":
            lock_state = notification.core.lock_state_changed
            print(f"<core, notif> LOCK STATE: {errors.LOCKSTATE[lock_state]}")
            return
        print("<err> Invalid notification type")
        return

    if notification_subsystem == "keymap":
        keymap_notification_type = notification.keymap.WhichOneof("notification_type")
        if keymap_notification_type == "unsaved_changes_status_changed":
            unsaved_changes_status_changed = (
                notification.keymap.unsaved_changes_status_changed
            )
            print("<keymap, notif> Unsaved changes status changed:")
            print(unsaved_changes_status_changed)
            return
        print("<err> Invalid notification type")
        return

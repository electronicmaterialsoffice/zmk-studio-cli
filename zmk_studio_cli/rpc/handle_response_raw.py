# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
ZMK Studio RPC Protocol response handler
"""

import google.protobuf

from ..logger import log_err
from ..proto import studio_pb2 as studio
from .subsystems.behaviors import handle_request_response_behaviors
from .subsystems.core import handle_notification_core, handle_request_response_core
from .subsystems.haptics import handle_request_response_haptics
from .subsystems.keymap import (
    handle_notification_keymap,
    handle_request_response_keymap,
)
from .subsystems.meta import handle_request_response_meta


def handle_response_raw(response_msg: bytes):
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
        handle_request_response_meta(request_response.meta)
    if req_response_subsystem == "core":
        handle_request_response_core(request_response.core)
    if req_response_subsystem == "behaviors":
        handle_request_response_behaviors(request_response.behaviors)
    if req_response_subsystem == "keymap":
        handle_request_response_keymap(request_response.keymap)
    if req_response_subsystem == "haptics":
        handle_request_response_haptics(request_response.haptics)


def handle_notification(notification: studio.Notification):
    """Handle Notification message from ZMK Studio RPC Protocol"""
    notification_subsystem = notification.WhichOneof("subsystem")

    if notification_subsystem == "core":
        handle_notification_core(notification.core)
    if notification_subsystem == "keymap":
        handle_notification_keymap(notification.keymap)

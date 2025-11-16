# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
ZMK Studio RPC Protocol functions
"""

import google.protobuf
import serial

from .logger import log_err
from .proto import studio_pb2 as studio
from .subsystems.meta import handle_request_response_meta
from .subsystems.core import handle_request_response_core, handle_notification_core
from .subsystems.behaviors import handle_request_response_behaviors
from .subsystems.keymap import (
    handle_request_response_keymap,
    handle_notification_keymap,
)

RPC_SOF = b"\xab"
RPC_ESC = b"\xac"
RPC_EOF = b"\xad"


def send_request(ser: serial.Serial, request: bytes, verbose: bool = False):
    """Send Request message via ZMK Studio RPC Protocol"""
    request_msg = b""
    request_msg = request_msg + RPC_SOF
    for request_chr in request.SerializeToString():
        request_byte = request_chr.to_bytes()
        if request_byte in (RPC_SOF, RPC_ESC, RPC_EOF):
            request_msg = request_msg + RPC_ESC
        request_msg = request_msg + request_byte
    request_msg = request_msg + RPC_EOF

    if verbose is True:
        print("<request>", request_msg)
    ser.write(request_msg)


def get_response(ser: serial.Serial, verbose: bool = False):
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
        print("<response>", response_msg)
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
        handle_request_response_meta(request_response.meta)
    if req_response_subsystem == "core":
        handle_request_response_core(request_response.core)
    if req_response_subsystem == "behaviors":
        handle_request_response_behaviors(request_response.behaviors)
    if req_response_subsystem == "keymap":
        handle_request_response_keymap(request_response.keymap)


def handle_notification(notification: studio.Notification):
    """Handle Notification message from ZMK Studio RPC Protocol"""
    notification_subsystem = notification.WhichOneof("subsystem")

    if notification_subsystem == "core":
        handle_notification_core(notification.core)
    if notification_subsystem == "keymap":
        handle_notification_keymap(notification.keymap)

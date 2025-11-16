# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio RPC Protocol functions"""

import serial

from .get_response_raw import get_response_raw
from .handle_response_raw import handle_response_raw
from .send_request_raw import send_request_raw


def rpc_send_request(ser: serial.Serial, request: bytes, verbose: bool = False):
    """Send Request message via ZMK Studio RPC Protocol"""
    return send_request_raw(ser=ser, request=request, verbose=verbose)


def rpc_get_response(ser: serial.Serial, verbose: bool = False):
    """Get Response mesage from ZMK Studio RPC Protocol"""
    return get_response_raw(ser=ser, verbose=verbose)


def rpc_handle_response(response_msg: bytes):
    """Handle Response message from ZMK Studio RPC Protocol"""
    return handle_response_raw(response_msg=response_msg)

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""ZMK Studio RPC Protocol send request"""

import serial

from .special_characters import RPC_EOF, RPC_ESC, RPC_SOF


def send_request_raw(ser: serial.Serial, request: bytes, verbose: bool = False):
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
    return ser.write(request_msg)

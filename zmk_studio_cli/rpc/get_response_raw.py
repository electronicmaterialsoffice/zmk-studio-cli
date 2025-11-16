# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""ZMK Studio RPC Protocol get response"""

import serial

from .special_characters import RPC_EOF, RPC_ESC, RPC_SOF


def get_response_raw(ser: serial.Serial, verbose: bool = False):
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

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

import serial
from ..proto import studio_pb2 as studio
from ..rpc import send_request, get_response, handle_response


def get_device_info(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 1
    request.core.get_device_info = True
    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def get_lock_state(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 2
    request.core.get_lock_state = True
    send_request(ser, request)
    handle_response(get_response(ser, verbose))


# Todo: Review lock command
def lock(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 3
    request.core.lock = True
    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def reset_settings(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 4
    request.core.reset_settings = True
    send_request(ser, request)
    handle_response(get_response(ser, verbose))

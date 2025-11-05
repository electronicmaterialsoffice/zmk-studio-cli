# Copyright (c) 2025 Electronic Materials Office Ltd.
# SPDX-License-Identifier: MIT

import serial
from ..proto import studio_pb2 as studio
from ..rpc import send_request, get_response, handle_response


def list_all_behaviors(ser: serial.Serial, verbose: bool):
    """Send behavior Request to list all behaviors"""
    request = studio.Request()
    request.request_id = 1
    request.behaviors.list_all_behaviors = True
    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def get_behavior_details(ser: serial.Serial, behavior_id: int | None, verbose: bool):
    """Send behavior Request to get behavior details"""
    request = studio.Request()
    request.request_id = 2
    request.behaviors.get_behavior_details.behavior_id = behavior_id
    send_request(ser, request)
    handle_response(get_response(ser, verbose))

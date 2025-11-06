# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
get-device-info
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def core_get_device_info(ctx: typer.Context) -> None:
    """Get keyboard name and serial number"""
    ser = ctx.obj
    request = studio.Request()
    request.request_id = 1
    request.core.get_device_info = True
    send_request(ser, request)
    handle_response(get_response(ser, False))

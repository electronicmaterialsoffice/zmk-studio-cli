# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
backlight-get-brightness
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def backlight_get_brightness(ctx: typer.Context) -> None:
    """Get backlight brightness"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 5
    request.backlight.backlight_get_brightness = True
    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

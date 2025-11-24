# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
backlight-is-on
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def backlight_is_on(ctx: typer.Context) -> None:
    """Get backlight state"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 4
    request.backlight.backlight_is_on = True
    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

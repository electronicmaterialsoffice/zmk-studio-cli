# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
backlight-set-brightness
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def backlight_set_brightness(
    ctx: typer.Context,
    brightness: Annotated[
        int | None,
        typer.Argument(
            help="Brightness",
        ),
    ] = None,
) -> None:
    """Set backlight brightness"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 6
    request.backlight.backlight_set_brightness = brightness
    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

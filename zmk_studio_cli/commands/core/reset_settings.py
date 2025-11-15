# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
reset-settings
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def core_reset_settings(ctx: typer.Context) -> None:
    """Reset keyboard's ZMK Studio settings"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 4
    request.core.reset_settings = True
    send_request(ser=ser, request=request, verbose=verbose)
    handle_response(get_response(ser=ser, verbose=verbose))

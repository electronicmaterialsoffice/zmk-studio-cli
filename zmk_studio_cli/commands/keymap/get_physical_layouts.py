# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
get-physical-layouts
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def keymap_get_physical_layouts(ctx: typer.Context) -> None:
    """Get physial layouts"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 6
    request.keymap.get_physical_layouts = True

    send_request(ser=ser, request=request, verbose=verbose)
    handle_response(get_response(ser=ser, verbose=verbose))

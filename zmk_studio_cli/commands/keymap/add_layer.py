# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
add-layer
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def keymap_add_layer(ctx: typer.Context) -> None:
    """Add layer to keymap"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 9
    request.keymap.add_layer.SetInParent()

    send_request(ser=ser, request=request, verbose=verbose)
    handle_response(get_response(ser=ser, verbose=verbose))

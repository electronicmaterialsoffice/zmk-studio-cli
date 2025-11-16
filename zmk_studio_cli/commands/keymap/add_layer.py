# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
add-layer
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def keymap_add_layer(ctx: typer.Context) -> None:
    """Add layer to keymap"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 9
    request.keymap.add_layer.SetInParent()

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

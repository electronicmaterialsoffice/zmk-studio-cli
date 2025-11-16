# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
remove-layer
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def keymap_remove_layer(
    ctx: typer.Context,
    layer_index: Annotated[
        int | None,
        typer.Argument(
            help="Layer index",
        ),
    ] = None,
) -> None:
    """Remove layer"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 10
    request.keymap.remove_layer.layer_index = layer_index

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
move-layer
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def keymap_move_layer(
    ctx: typer.Context,
    start_index: Annotated[
        int | None,
        typer.Argument(
            help="Layer move start index",
        ),
    ] = None,
    dest_index: Annotated[
        int | None,
        typer.Argument(
            help="Layer move destination index",
        ),
    ] = None,
) -> None:
    """Move layer from start to dest index"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 8
    request.keymap.move_layer.start_index = start_index
    request.keymap.move_layer.dest_index = dest_index

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

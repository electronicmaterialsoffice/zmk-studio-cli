# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
remove-layer
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


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
    ser = ctx.obj
    request = studio.Request()
    request.request_id = 10
    request.keymap.remove_layer.layer_index = layer_index

    send_request(ser, request)
    handle_response(get_response(ser, False))

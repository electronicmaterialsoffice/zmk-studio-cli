# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
restore-layer
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def keymap_restore_layer(
    ctx: typer.Context,
    layer_id: Annotated[
        int | None,
        typer.Argument(
            help="Layer ID",
        ),
    ] = None,
    at_index: Annotated[
        int | None,
        typer.Argument(
            help="Target layer index",
        ),
    ] = None,
) -> None:
    """Restore layer with ID at chosen index"""
    ser = ctx.obj
    request = studio.Request()
    request.request_id = 11
    request.keymap.restore_layer.layer_id = layer_id
    request.keymap.restore_layer.at_index = at_index

    send_request(ser, request)
    handle_response(get_response(ser, False))

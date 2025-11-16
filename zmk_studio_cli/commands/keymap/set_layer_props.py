# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
set-layer-props
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def keymap_set_layer_props(
    ctx: typer.Context,
    layer_id: Annotated[
        int | None,
        typer.Argument(
            help="Layer ID",
        ),
    ] = None,
    layer_name: Annotated[
        str | None,
        typer.Argument(
            help="Layer name",
        ),
    ] = None,
) -> None:
    """Set layer properties (name)"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 12
    request.keymap.set_layer_props.layer_id = layer_id
    request.keymap.set_layer_props.name = layer_name

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser, verbose=verbose))

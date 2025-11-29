# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
layer-deactivate
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def keymap_layer_deactivate(
    ctx: typer.Context,
    layer_id: Annotated[
        int | None,
        typer.Argument(
            help="Layer ID",
        ),
    ] = None,
    locking: Annotated[
        bool | None,
        typer.Argument(
            help="Locking",
        ),
    ] = None,
) -> None:
    """Deactivate layer"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 16
    request.keymap.layer_deactivate.layer_id = layer_id
    request.keymap.layer_deactivate.locking = locking

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser, verbose=verbose))

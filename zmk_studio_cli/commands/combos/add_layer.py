# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
add-layer
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def combos_add_layer(
    ctx: typer.Context,
    combo_id: Annotated[
        int,
        typer.Argument(
            help="Combo identifier",
        ),
    ] = None,
    layer: Annotated[
        int,
        typer.Argument(
            help="Layer",
        ),
    ] = None,
) -> None:
    """Remove layer from a combo"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 1
    request.combos.set_combo_layer_state.id = combo_id
    request.combos.set_combo_layer_state.layer = layer
    request.combos.set_combo_layer_state.enabled = True

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

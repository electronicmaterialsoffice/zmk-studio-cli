# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
clear-layers
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def combos_clear_layers(
    ctx: typer.Context,
    combo_id: Annotated[
        int,
        typer.Argument(
            help="Combo identifier",
        ),
    ] = None,
) -> None:
    """Clear layers from a combo"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 1
    request.combos.clear_combo_layers.id = combo_id

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

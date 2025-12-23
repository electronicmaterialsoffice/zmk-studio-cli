# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
add-position
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def combos_add_position(
    ctx: typer.Context,
    combo_id: Annotated[
        int | None,
        typer.Argument(
            help="Combo identifier",
        ),
    ] = None,
    key_pos: Annotated[
        int | None,
        typer.Argument(
            help="Key Position",
        ),
    ] = None,
) -> None:
    """Add key position to a combo"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 1
    request.combos.set_combo_position_state.id = combo_id
    request.combos.set_combo_position_state.position = key_pos
    request.combos.set_combo_position_state.enabled = True

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))



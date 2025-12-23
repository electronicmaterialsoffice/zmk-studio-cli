# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
add-combo
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def combos_add_combo(
    ctx: typer.Context,
    behavior_id: Annotated[
        int,
        typer.Argument(
            help="Behavior ID",
        ),
    ] = None,
    param1: Annotated[
        int,
        typer.Argument(
            help="Behavior 1st parameter",
        ),
    ] = None,
    param2: Annotated[
        int,
        typer.Argument(
            help="Behavior 1st parameter",
        ),
    ] = None,
    key_position1: Annotated[
        int,
        typer.Argument(
            help="Key position #1",
        ),
    ] = None,
    key_position2: Annotated[
        int,
        typer.Argument(
            help="Key position #1",
        ),
    ] = None,
) -> None:
    """Add a combo"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 1
    request.combos.add_combo.binding.behavior_id = behavior_id
    if param1:
        request.combos.add_combo.binding.param1 = param1
    if param2:
        request.combos.add_combo.binding.param2 = param2

    request.combos.add_combo.positions.append(key_position1)
    request.combos.add_combo.positions.append(key_position2)

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
set-binding
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def combos_set_binding(
    ctx: typer.Context,
    combo_id: Annotated[
        int,
        typer.Argument(
            help="Combo identifier",
        ),
    ] = None,
    behavior_id: Annotated[
        int,
        typer.Argument(
            help="Behavior ID",
        ),
    ] = None,
    param1: Annotated[
        int | None,
        typer.Argument(
            help="Behavior 1st parameter",
        ),
    ] = None,
    param2: Annotated[
        int | None,
        typer.Argument(
            help="Behavior 1st parameter",
        ),
    ] = None,
) -> None:
    """Set a combo's binding"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 1
    request.combos.set_combo_binding.id = combo_id
    request.combos.set_combo_binding.binding.behavior_id = behavior_id
    if param1:
        request.combos.set_combo_binding.binding.param1 = param1
    if param2:
        request.combos.set_combo_binding.binding.param2 = param2

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

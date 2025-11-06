# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
set-layer-binding
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def keymap_set_layer_binding(
    ctx: typer.Context,
    layer_id: Annotated[
        int | None,
        typer.Argument(
            help="Layer ID",
        ),
    ] = None,
    key_position: Annotated[
        int | None,
        typer.Argument(
            help="Key position",
        ),
    ] = None,
    behavior_id: Annotated[
        int | None,
        typer.Argument(
            help="Behavior ID",
        ),
    ] = None,
    param1: Annotated[
        int | None,
        typer.Argument(
            help="Behavior param1",
        ),
    ] = None,
    param2: Annotated[
        int | None,
        typer.Argument(
            help="Behavior param2",
        ),
    ] = None,
) -> None:
    """Set keymap binding on chosen layer"""
    ser = ctx.obj
    request = studio.Request()
    request.request_id = 2
    request.keymap.set_layer_binding.layer_id = layer_id
    request.keymap.set_layer_binding.key_position = key_position
    request.keymap.set_layer_binding.binding.behavior_id = behavior_id
    request.keymap.set_layer_binding.binding.param1 = param1
    request.keymap.set_layer_binding.binding.param2 = param2

    send_request(ser, request)
    handle_response(get_response(ser, False))

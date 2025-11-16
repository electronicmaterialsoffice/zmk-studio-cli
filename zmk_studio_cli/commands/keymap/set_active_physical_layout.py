# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
set-active-physical-layout
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def keymap_set_active_physical_layout(
    ctx: typer.Context,
    layout: Annotated[
        int | None,
        typer.Argument(
            help="Active physical layout",
        ),
    ] = None,
) -> None:
    """Set active physical layout"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 7
    request.keymap.set_active_physical_layout = layout

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
set-active-physical-layout
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


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
    ser = ctx.obj
    request = studio.Request()
    request.request_id = 7
    request.keymap.set_active_physical_layout = layout

    send_request(ser, request)
    handle_response(get_response(ser, False))

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
play-indicator
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def play_indicator(
    ctx: typer.Context,
    indicator: Annotated[
        int | None,
        typer.Argument(
            help="Key position",
        ),
    ] = None,
) -> None:
    """Play indicator"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 3
    request.altar_ii.play_indicator = indicator
    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

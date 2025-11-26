# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
als-set-state
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def als_set_state(
    ctx: typer.Context,
    als_state: Annotated[
        int | None,
        typer.Argument(
            help="ALS State",
        ),
    ] = None,
) -> None:
    """Get haptics rated voltage"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 2
    request.altar_ii.als_set_state = als_state
    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

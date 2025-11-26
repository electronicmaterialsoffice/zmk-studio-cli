# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
haptics-set-rated-voltage
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def haptics_set_rated_voltage(
    ctx: typer.Context,
    rated_voltage: Annotated[
        int | None,
        typer.Argument(
            help="Rated Voltage",
        ),
    ] = None,
) -> None:
    """Set haptics rated voltage"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 6
    request.haptics.haptics_set_rated_voltage = rated_voltage
    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

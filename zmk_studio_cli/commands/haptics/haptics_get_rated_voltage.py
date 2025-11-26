# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
haptics-get-rated-voltage
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def haptics_get_rated_voltage(ctx: typer.Context) -> None:
    """Get haptics rated voltage"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 5
    request.haptics.haptics_get_rated_voltage = True
    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

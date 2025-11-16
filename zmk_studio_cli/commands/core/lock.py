# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
lock
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def core_lock(ctx: typer.Context) -> None:
    """Lock the connected keyboard"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 3
    request.core.lock = True
    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
get-lock-state
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def core_get_lock_state(ctx: typer.Context) -> None:
    """Get keyboard lock state"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 2
    request.core.get_lock_state = True
    send_request(ser=ser, request=request, verbose=verbose)
    handle_response(get_response(ser=ser, verbose=verbose))

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
discard-changes
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def core_discard_changes(ctx: typer.Context) -> None:
    """Discard unsaved changes on the device"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 2
    request.core.discard_changes = True
    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

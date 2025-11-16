# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
check-unsaved-changes
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def keymap_check_unsaved_changes(ctx: typer.Context) -> None:
    """Check for unsaved keymap changes"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 3
    request.keymap.check_unsaved_changes = True

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

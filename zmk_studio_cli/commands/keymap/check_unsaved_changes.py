# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
check-unsaved-changes
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def keymap_check_unsaved_changes(ctx: typer.Context) -> None:
    """Check for unsaved keymap changes"""
    ser = ctx.obj
    request = studio.Request()
    request.request_id = 3
    request.keymap.check_unsaved_changes = True

    send_request(ser, request)
    handle_response(get_response(ser, False))

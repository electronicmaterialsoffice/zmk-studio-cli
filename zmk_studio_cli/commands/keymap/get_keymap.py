# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
get-keymap
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def keymap_get_keymap(ctx: typer.Context) -> None:
    """Get keymap"""
    ser = ctx.obj
    request = studio.Request()
    request.request_id = 1
    request.keymap.get_keymap = True

    send_request(ser, request)
    handle_response(get_response(ser, False))

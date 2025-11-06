# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
list-all-behaviors
"""

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def behaviors_list_all_behaviors(ctx: typer.Context) -> None:
    """Retrieve all stored behavior IDs"""
    ser = ctx.obj
    request = studio.Request()
    request.request_id = 1
    request.behaviors.list_all_behaviors = True
    send_request(ser, request)
    handle_response(get_response(ser, False))

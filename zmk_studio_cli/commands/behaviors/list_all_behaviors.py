# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
list-all-behaviors
"""

import typer

from ...logger import log_dbg
from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def behaviors_list_all_behaviors(ctx: typer.Context) -> None:
    """Retrieve all stored behavior IDs"""
    ser = ctx.obj
    request = studio.Request()
    request.request_id = 1
    request.behaviors.list_all_behaviors = True
    send_request(ser, request)

    response_msg = get_response(ser, False)
    response = studio.Response()
    response.ParseFromString(response_msg)

    behavior_list = response.request_response.behaviors.list_all_behaviors.behaviors
    for behavior_id in behavior_list:
        behavior_request = studio.Request()
        behavior_request.request_id = 2
        behavior_request.behaviors.get_behavior_details.behavior_id = behavior_id
        send_request(ser, behavior_request)

        behavior_response_msg = get_response(ser, False)
        behavior_response = studio.Response()
        behavior_response.ParseFromString(behavior_response_msg)
        behavior_details = (
            behavior_response.request_response.behaviors.get_behavior_details
        )
        behavior_display_name = behavior_details.display_name
        log_dbg("behaviors", f"Behavior ID: {behavior_id: 3} {behavior_display_name}")

    # handle_response(response_msg)

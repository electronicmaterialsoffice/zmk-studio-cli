# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
get-behavior-details
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import get_response, handle_response, send_request


def behaviors_get_behavior_details(
    ctx: typer.Context,
    behavior_id: Annotated[
        int | None,
        typer.Argument(
            help="Behavior ID",
        ),
    ] = None,
) -> None:
    """Get behavior name/metadata from ID"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 2
    request.behaviors.get_behavior_details.behavior_id = behavior_id
    send_request(ser=ser, request=request, verbose=verbose)
    handle_response(get_response(ser=ser, verbose=verbose))

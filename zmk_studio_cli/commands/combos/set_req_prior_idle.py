# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
set-req-prior-idle
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def combos_set_req_prior_idle(
    ctx: typer.Context,
    combo_id: Annotated[
        int,
        typer.Argument(
            help="Combo identifier",
        ),
    ] = None,
    req_prior_idle: Annotated[
        int,
        typer.Argument(
            help="Require prior idle (ms)",
        ),
    ] = None,
) -> None:
    """Set combo timeout"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 1
    request.combos.set_combo_require_prior_idle.id = combo_id
    request.combos.set_combo_require_prior_idle.require_prior_idle = req_prior_idle

    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

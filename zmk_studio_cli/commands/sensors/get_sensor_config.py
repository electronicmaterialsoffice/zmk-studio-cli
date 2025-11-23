# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
get-sensor-config
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def sensors_get_sensor_config(
    ctx: typer.Context,
    sensor_index: Annotated[
        int | None,
        typer.Argument(
            help="Sensor index",
        ),
    ] = None,
) -> None:
    """Get sensor config for chosen sensor index"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 3
    request.sensors.get_sensor_config = sensor_index
    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

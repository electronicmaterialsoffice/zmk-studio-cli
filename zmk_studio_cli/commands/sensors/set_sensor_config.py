# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
set-sensor-config
"""

from typing import Annotated

import typer

from ...proto import studio_pb2 as studio
from ...rpc import rpc_get_response, rpc_handle_response, rpc_send_request


def sensors_set_sensor_config(
    ctx: typer.Context,
    sensor_index: Annotated[
        int | None,
        typer.Argument(
            help="Sensor index",
        ),
    ] = None,
    triggers_per_rotation: Annotated[
        int | None,
        typer.Argument(
            help="Triggers per rotation",
        ),
    ] = None,
) -> None:
    """Set sensor config for chosen sensor index"""
    ser = ctx.obj.ser
    verbose = ctx.obj.verbose

    request = studio.Request()
    request.request_id = 4
    request.sensors.set_sensor_config.sensor_index = sensor_index
    request.sensors.set_sensor_config.triggers_per_rotation = triggers_per_rotation
    rpc_send_request(ser=ser, request=request, verbose=verbose)
    rpc_handle_response(rpc_get_response(ser=ser, verbose=verbose))

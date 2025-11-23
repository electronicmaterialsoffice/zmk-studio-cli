# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
ZMK Studio CLI sensor subcommands.
"""

import typer

from .get_sensor_binding import sensors_get_sensor_binding
from .get_sensor_config import sensors_get_sensor_config
from .set_sensor_binding import sensors_set_sensor_binding
from .set_sensor_config import sensors_set_sensor_config

app = typer.Typer(name="sensors")
app.command(name="get-sensor-binding")(sensors_get_sensor_binding)
app.command(name="set-sensor-binding")(sensors_set_sensor_binding)
app.command(name="get-sensor-config")(sensors_get_sensor_config)
app.command(name="set-sensor-config")(sensors_set_sensor_config)


@app.callback()
def core() -> None:
    """ZMK Studio sensors actions"""

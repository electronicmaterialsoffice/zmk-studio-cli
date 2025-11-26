# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
ZMK Studio CLI haptics subcommands.
"""

import typer

from .haptics_get_rated_voltage import haptics_get_rated_voltage
from .haptics_is_on import haptics_is_on
from .haptics_off import haptics_off
from .haptics_on import haptics_on
from .haptics_set_rated_voltage import haptics_set_rated_voltage
from .haptics_toggle import haptics_toggle

app = typer.Typer(name="haptics")
app.command(name="on")(haptics_on)
app.command(name="off")(haptics_off)
app.command(name="toggle")(haptics_toggle)
app.command(name="is-on")(haptics_is_on)
app.command(name="get-rated-voltage")(haptics_get_rated_voltage)
app.command(name="set-rated-voltage")(haptics_set_rated_voltage)


@app.callback()
def core() -> None:
    """ZMK Studio haptics actions"""

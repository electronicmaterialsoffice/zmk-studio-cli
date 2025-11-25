# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
ZMK Studio CLI backlight subcommands.
"""

import typer

from .backlight_get_brightness import backlight_get_brightness
from .backlight_is_on import backlight_is_on
from .backlight_off import backlight_off
from .backlight_on import backlight_on
from .backlight_set_brightness import backlight_set_brightness
from .backlight_toggle import backlight_toggle

app = typer.Typer(name="backlight")
app.command(name="on")(backlight_on)
app.command(name="off")(backlight_off)
app.command(name="toggle")(backlight_toggle)
app.command(name="is-on")(backlight_is_on)
app.command(name="get-brightness")(backlight_get_brightness)
app.command(name="set-brightness")(backlight_set_brightness)


@app.callback()
def core() -> None:
    """ZMK Studio backlight actions"""

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
ZMK Studio CLI Altar II subcommands.
"""

import typer

from .als_get_state import als_get_state
from .als_set_state import als_set_state
from .play_indicator import play_indicator

app = typer.Typer(name="altar_ii")
app.command(name="als-get-state")(als_get_state)
app.command(name="als-set-state")(als_set_state)
app.command(name="play-indicator")(play_indicator)


@app.callback()
def core() -> None:
    """ZMK Studio Altar II actions"""

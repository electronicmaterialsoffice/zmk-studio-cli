# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
ZMK Studio CLI Commands.
"""

import typer

from . import behaviors, core, haptics, keymap


def register(app: typer.Typer) -> None:
    """Register all commands with the app"""
    app.add_typer(core.app)
    app.add_typer(behaviors.app)
    app.add_typer(keymap.app)
    app.add_typer(haptics.app)

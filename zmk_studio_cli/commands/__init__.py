"""
ZMK Studio CLI Commands.
"""

import typer

from . import core, behaviors, keymap


def register(app: typer.Typer) -> None:
    """Register all commands with the app"""
    app.add_typer(core.app)
    app.add_typer(behaviors.app)
    app.add_typer(keymap.app)

"""
reset-settings
"""

import typer
from ...subsystems import core


def core_reset_settings(ctx: typer.Context) -> None:
    """Reset keyboard's ZMK Studio settings"""
    ser = ctx.obj
    core.reset_settings(ser, verbose=False)

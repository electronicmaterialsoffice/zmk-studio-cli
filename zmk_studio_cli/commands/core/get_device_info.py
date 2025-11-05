"""
get-device-info
"""

import typer
from ...subsystems import core


def core_get_device_info(ctx: typer.Context) -> None:
    """Get keyboard name and serial number"""
    ser = ctx.obj
    core.get_device_info(ser, verbose=False)

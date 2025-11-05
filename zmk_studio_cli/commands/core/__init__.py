"""
ZMK Studio CLI core subcommands.
"""

import typer

from .get_device_info import core_get_device_info
from .get_lock_state import core_get_lock_state
from .lock import core_lock
from .reset_settings import core_reset_settings

app = typer.Typer(name="core")
app.command(name="get-device-info")(core_get_device_info)
app.command(name="get-lock-state")(core_get_lock_state)
app.command(name="lock")(core_lock)
app.command(name="reset-settings")(core_reset_settings)


@app.callback()
def core() -> None:
    """ZMK Studio core actions"""

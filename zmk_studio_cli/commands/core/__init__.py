# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
ZMK Studio CLI core subcommands.
"""

import typer

from .get_device_info import core_get_device_info
from .get_lock_state import core_get_lock_state
from .lock import core_lock
from .reset_settings import core_reset_settings
from .check_unsaved_changes import core_check_unsaved_changes
from .save_changes import core_save_changes
from .discard_changes import core_discard_changes

app = typer.Typer(name="core")
app.command(name="get-device-info")(core_get_device_info)
app.command(name="get-lock-state")(core_get_lock_state)
app.command(name="lock")(core_lock)
app.command(name="reset-settings")(core_reset_settings)
app.command(name="check-unsaved-changes")(core_check_unsaved_changes)
app.command(name="save-changes")(core_save_changes)
app.command(name="discard-changes")(core_discard_changes)


@app.callback()
def core() -> None:
    """ZMK Studio core actions"""

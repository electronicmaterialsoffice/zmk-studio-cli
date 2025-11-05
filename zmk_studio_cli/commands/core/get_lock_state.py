# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
get-lock-state
"""

import typer
from ...subsystems import core


def core_get_lock_state(ctx: typer.Context) -> None:
    """Get keyboard lock state"""
    ser = ctx.obj
    core.get_lock_state(ser, verbose=False)

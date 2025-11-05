# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
lock
"""

import typer
from ...subsystems import core


def core_lock(ctx: typer.Context) -> None:
    """Lock the connected keyboard"""
    ser = ctx.obj
    core.lock(ser, verbose=False)

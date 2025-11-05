# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
save-changes
"""

import typer
from ...subsystems import keymap


def keymap_save_changes(ctx: typer.Context) -> None:
    """Save keymap changes"""
    ser = ctx.obj
    keymap.save_changes(ser, verbose=False)

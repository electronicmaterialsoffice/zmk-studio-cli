# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
get-physical-layouts
"""

import typer
from ...subsystems import keymap


def keymap_get_physical_layouts(ctx: typer.Context) -> None:
    """Get physial layouts"""
    ser = ctx.obj
    keymap.get_physical_layouts(ser, verbose=False)

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
get-keymap
"""

import typer
from ...subsystems import keymap


def keymap_get_keymap(ctx: typer.Context) -> None:
    """Get keymap"""
    ser = ctx.obj
    keymap.get_keymap(ser, verbose=False)

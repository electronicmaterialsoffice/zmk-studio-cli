# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
"zmk-studio-cli keymap get-keymap" command.
"""

from typing import Annotated

import typer
from ...subsystems import keymap


def keymap_set_active_physical_layout(
    ctx: typer.Context,
    layout: Annotated[
        int | None,
        typer.Argument(
            help="Active physical layout",
        ),
    ] = None,
) -> None:
    """Set active physical layout"""
    ser = ctx.obj
    keymap.set_active_physical_layout(ser, layout, verbose=False)

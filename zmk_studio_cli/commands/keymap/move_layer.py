# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
move-layer
"""

from typing import Annotated

import typer
from ...subsystems import keymap


def keymap_move_layer(
    ctx: typer.Context,
    start_index: Annotated[
        int | None,
        typer.Argument(
            help="Layer move start index",
        ),
    ] = None,
    dest_index: Annotated[
        int | None,
        typer.Argument(
            help="Layer move destination index",
        ),
    ] = None,
) -> None:
    """Move layer from start to dest index"""
    ser = ctx.obj
    keymap.move_layer(ser, start_index, dest_index, verbose=False)

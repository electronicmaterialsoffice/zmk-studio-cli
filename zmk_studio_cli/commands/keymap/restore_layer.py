# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
restore-layer
"""

from typing import Annotated

import typer
from ...subsystems import keymap


def keymap_restore_layer(
    ctx: typer.Context,
    layer_id: Annotated[
        int | None,
        typer.Argument(
            help="Layer ID",
        ),
    ] = None,
    at_index: Annotated[
        int | None,
        typer.Argument(
            help="Target layer index",
        ),
    ] = None,
) -> None:
    """Restore layer with ID at chosen index"""
    ser = ctx.obj
    keymap.restore_layer(ser, layer_id, at_index, verbose=False)

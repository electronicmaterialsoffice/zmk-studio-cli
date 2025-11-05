"""
remove-layer
"""

from typing import Annotated

import typer
from ...subsystems import keymap


def keymap_remove_layer(
    ctx: typer.Context,
    layer_index: Annotated[
        int | None,
        typer.Argument(
            help="Layer index",
        ),
    ] = None,
) -> None:
    """Remove layer"""
    ser = ctx.obj
    keymap.remove_layer(ser, layer_index, verbose=False)

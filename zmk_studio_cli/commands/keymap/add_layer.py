"""
add-layer
"""

import typer
from ...subsystems import keymap


def keymap_add_layer(ctx: typer.Context) -> None:
    """Add layer to keymap"""
    ser = ctx.obj
    keymap.add_layer(ser, verbose=False)

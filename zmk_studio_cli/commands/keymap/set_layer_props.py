"""
"zmk-studio-cli keymap get-keymap" command.
"""

from typing import Annotated

import typer
from ...subsystems import keymap


def keymap_set_layer_props(
    ctx: typer.Context,
    layer_id: Annotated[
        int | None,
        typer.Argument(
            help="Layer ID",
        ),
    ] = None,
    layer_name: Annotated[
        str | None,
        typer.Argument(
            help="Layer name",
        ),
    ] = None,
) -> None:
    """Set layer properties (name)"""
    ser = ctx.obj
    keymap.set_layer_props(ser, layer_id, layer_name, verbose=False)

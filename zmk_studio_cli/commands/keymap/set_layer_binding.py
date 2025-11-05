"""
"zmk-studio-cli keymap get-keymap" command.
"""

from typing import Annotated

import typer
from ...subsystems import keymap


def keymap_set_layer_binding(
    ctx: typer.Context,
    layer_id: Annotated[
        int | None,
        typer.Argument(
            help="Layer ID",
        ),
    ] = None,
    key_position: Annotated[
        int | None,
        typer.Argument(
            help="Key position",
        ),
    ] = None,
    behavior_id: Annotated[
        int | None,
        typer.Argument(
            help="Behavior ID",
        ),
    ] = None,
    param1: Annotated[
        int | None,
        typer.Argument(
            help="Behavior param1",
        ),
    ] = None,
    param2: Annotated[
        int | None,
        typer.Argument(
            help="Behavior param2",
        ),
    ] = None,
) -> None:
    """Set keymap binding on chosen layer"""
    ser = ctx.obj
    binding = keymap.BehaviorBinding(behavior_id, param1, param2)
    keymap.set_layer_binding(ser, layer_id, key_position, binding, verbose=False)

"""
discard-changes
"""

import typer
from ...subsystems import keymap


def keymap_discard_changes(
    ctx: typer.Context,
) -> None:
    """Discard keymap changes"""
    ser = ctx.obj
    keymap.discard_changes(ser, verbose=False)

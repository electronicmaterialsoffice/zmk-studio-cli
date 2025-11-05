"""
save-changes
"""

import typer
from ...subsystems import keymap


def keymap_save_changes(ctx: typer.Context) -> None:
    """Save keymap changes"""
    ser = ctx.obj
    keymap.save_changes(ser, verbose=False)

"""
check-unsaved-changes
"""

import typer
from ...subsystems import keymap


def keymap_check_unsaved_changes(ctx: typer.Context) -> None:
    """Check for unsaved keymap changes"""
    ser = ctx.obj
    keymap.check_unsaved_changes(ser, verbose=False)

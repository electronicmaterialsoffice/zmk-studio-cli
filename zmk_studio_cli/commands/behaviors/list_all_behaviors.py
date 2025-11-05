"""
list-all-behaviors
"""

import typer
from ...subsystems import behaviors


def behaviors_list_all_behaviors(ctx: typer.Context) -> None:
    """Retrieve all stored behavior IDs"""
    ser = ctx.obj
    behaviors.list_all_behaviors(ser, verbose=False)

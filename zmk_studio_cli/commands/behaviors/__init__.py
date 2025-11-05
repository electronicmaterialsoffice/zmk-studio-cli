"""
ZMK Studio CLI behavior subcommands.
"""

import typer

from .list_all_behaviors import behaviors_list_all_behaviors
from .get_behavior_details import behaviors_get_behavior_details

app = typer.Typer(name="behaviors")
app.command(name="list-all-behaviors")(behaviors_list_all_behaviors)
app.command(name="get-behavior-details")(behaviors_get_behavior_details)


@app.callback()
def behaviors() -> None:
    """ZMK Studio behavior actions"""

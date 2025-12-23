# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
ZMK Studio CLI combos subcommands.
"""

import typer

from .get_combos import combos_get_combos
from .add_combo import combos_add_combo
from .delete_combo import combos_delete_combo
from .set_binding import combos_set_binding
from .add_position import combos_add_position
from .remove_position import combos_remove_position
from .add_layer import combos_add_layer
from .remove_layer import combos_remove_layer
from .clear_layers import combos_clear_layers
from .set_slow_release import combos_set_slow_release
from .set_timeout import combos_set_timeout
from .set_req_prior_idle import combos_set_req_prior_idle

app = typer.Typer(name="combos")
app.command(name="get-combos")(combos_get_combos)
app.command(name="add-combo")(combos_add_combo)
app.command(name="delete-combo")(combos_delete_combo)
app.command(name="set-binding")(combos_set_binding)
app.command(name="add-position")(combos_add_position)
app.command(name="remove-position")(combos_remove_position)
app.command(name="add-layer")(combos_add_layer)
app.command(name="remove-layer")(combos_remove_layer)
app.command(name="clear-layers")(combos_clear_layers)
app.command(name="set-slow-release")(combos_set_slow_release)
app.command(name="set-timeout")(combos_set_timeout)
app.command(name="set-req-prior-idle")(combos_set_req_prior_idle)

@app.callback()
def combos() -> None:
    """ZMK Studio combos actions"""

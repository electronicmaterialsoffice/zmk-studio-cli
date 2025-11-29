# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
ZMK Studio CLI keymap subcommands.
"""

import typer

from .add_layer import keymap_add_layer
from .check_unsaved_changes import keymap_check_unsaved_changes
from .discard_changes import keymap_discard_changes
from .get_keymap import keymap_get_keymap
from .get_physical_layouts import keymap_get_physical_layouts
from .layer_activate import keymap_layer_activate
from .layer_active import keymap_layer_active
from .layer_deactivate import keymap_layer_deactivate
from .layer_locked import keymap_layer_locked
from .layer_to import keymap_layer_to
from .layer_toggle import keymap_layer_toggle
from .move_layer import keymap_move_layer
from .remove_layer import keymap_remove_layer
from .restore_layer import keymap_restore_layer
from .save_changes import keymap_save_changes
from .set_active_physical_layout import keymap_set_active_physical_layout
from .set_layer_binding import keymap_set_layer_binding
from .set_layer_props import keymap_set_layer_props

app = typer.Typer(name="keymap")
app.command(name="get-keymap")(keymap_get_keymap)
app.command(name="set-layer-binding")(keymap_set_layer_binding)
app.command(name="check-unsaved-changes")(keymap_check_unsaved_changes)
app.command(name="save-changes")(keymap_save_changes)
app.command(name="discard-changes")(keymap_discard_changes)
app.command(name="get-physical-layouts")(keymap_get_physical_layouts)
app.command(name="set-active-physical-layout")(keymap_set_active_physical_layout)
app.command(name="move-layer")(keymap_move_layer)
app.command(name="add-layer")(keymap_add_layer)
app.command(name="remove-layer")(keymap_remove_layer)
app.command(name="restore-layer")(keymap_restore_layer)
app.command(name="set-layer-props")(keymap_set_layer_props)
app.command(name="layer-active")(keymap_layer_active)
app.command(name="layer-locked")(keymap_layer_locked)
app.command(name="layer-activate")(keymap_layer_activate)
app.command(name="layer-deactivate")(keymap_layer_deactivate)
app.command(name="layer-toggle")(keymap_layer_toggle)
app.command(name="layer-to")(keymap_layer_to)


@app.callback()
def keymap() -> None:
    """ZMK Studio keymap actions"""

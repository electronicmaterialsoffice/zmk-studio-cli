# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
get-behavior-details
"""

from typing import Annotated

import typer
from ...subsystems import behaviors


def behaviors_get_behavior_details(
    ctx: typer.Context,
    behavior_id: Annotated[
        int | None,
        typer.Argument(
            help="Behavior ID",
        ),
    ] = None,
) -> None:
    """Get behavior name/metadata from ID"""
    ser = ctx.obj
    behaviors.get_behavior_details(ser, behavior_id, verbose=False)

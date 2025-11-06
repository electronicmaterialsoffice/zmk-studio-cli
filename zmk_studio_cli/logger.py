# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
rich logging for ZMK Studio CLI tool
"""

from rich.console import Console
from rich.style import Style

error_style = Style(color="red", bold=True)
notification_style = Style(color="light_sea_green", bold=True)
console = Console()


def log_dbg(subsystem: str, *args, **kwargs):
    """Print to console"""
    header = f"<dbg, {subsystem}>"
    console.print(header, *args, **kwargs, highlight=False)


def log_err(subsystem: str, *args, **kwargs):
    """Print to console with error style"""
    header = f"<err, {subsystem}>"
    console.print(header, *args, **kwargs, style=error_style, highlight=False)


def log_notif(subsystem: str, *args, **kwargs):
    """Print to console with notification style"""
    header = f"<notif, {subsystem}>"
    console.print(
        header,
        *args,
        **kwargs,
        style=notification_style,
        highlight=False,
    )

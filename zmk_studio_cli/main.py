# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

"""
CLI tool to interact with keyboards via ZMK Studio RPC Protocol
"""

from importlib import metadata
from typing import Annotated

import serial
import typer

from . import commands

app = typer.Typer(rich_markup_mode="rich")
commands.register(app)


def _version_callback(version: bool):
    if version:
        print(metadata.version("zmk-studio-cli"))
        raise typer.Exit()


@app.callback()
def main(
    ctx: typer.Context,
    port: Annotated[
        str,
        typer.Option(
            "--serial-port",
            "-p",
            help="Serial port to use with USB transport",
        ),
    ],
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose",
            help="Enable verbose printing of outbound requests and incoming responses",
        ),
    ] = False,
    _: Annotated[
        bool,
        typer.Option(
            "--version",
            "-v",
            help="Print version and exit.",
            callback=_version_callback,
            is_eager=True,
        ),
    ] = False,
) -> None:
    """
    ZMK Studio command line tool
    """
    ser = serial.Serial(port, timeout=timeoutDefaultSeconds)
    ctx.obj = Config(ser=ser, verbose=verbose)


timeoutDefaultSeconds = 10


class Config:

    def __init__(self, ser, verbose=False):
        self.ser = ser
        self.verbose = verbose

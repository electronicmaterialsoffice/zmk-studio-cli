"""
CLI tool to interact with ZMK Studio.
"""

from importlib import metadata
from typing import Annotated

import typer
import serial

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
    ser = serial.Serial(port)
    ctx.obj = ser

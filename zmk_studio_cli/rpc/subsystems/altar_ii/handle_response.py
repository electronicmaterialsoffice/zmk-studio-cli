# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""Altar II Response handler"""

from ....logger import log_dbg
from ....proto import altar_ii_pb2 as altar_ii
from .als import ALS_STATE


def handle_response(response: altar_ii.Response):
    """Handle behaviors Response from ZMK Studio RPC Protocol"""
    response_type = response.WhichOneof("response_type")
    if response_type == "als_get_state":
        handle_response_altar_ii_als_get_state(response=response)
    if response_type == "als_set_state":
        handle_response_altar_ii_als_set_state(response=response)
    if response_type == "play_indicator":
        handle_response_altar_ii_play_indicator(response=response)


def handle_response_altar_ii_als_get_state(response: altar_ii.Response):
    """Print altar_ii ALS get state"""
    log_dbg("altar_ii", f"ALS State: {ALS_STATE[response.als_get_state]}")


def handle_response_altar_ii_als_set_state(response: altar_ii.Response):
    """Print altar_ii ALS set state"""
    log_dbg("altar_ii", f"Set ALS state? {response.als_set_state}")


def handle_response_altar_ii_play_indicator(response: altar_ii.Response):
    """Print altar_ii play indicator result"""
    log_dbg("altar_ii", f"Playing indicator: {response.play_indicator}")

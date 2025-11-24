# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""backlight Response handler"""

from ....logger import log_dbg
from ....proto import backlight_pb2 as backlight


def handle_response(response: backlight.Response):
    """Handle behaviors Response from ZMK Studio RPC Protocol"""
    response_type = response.WhichOneof("response_type")
    if response_type == "backlight_on":
        handle_response_backlight_on(response=response)
    if response_type == "backlight_off":
        handle_response_backlight_off(response=response)
    if response_type == "backlight_toggle":
        handle_response_backlight_toggle(response=response)
    if response_type == "backlight_is_on":
        handle_response_backlight_is_on(response=response)
    if response_type == "backlight_get_brightness":
        handle_response_backlight_get_brightness(response=response)
    if response_type == "backlight_set_brightness":
        handle_response_backlight_set_brightness(response=response)


def handle_response_backlight_on(response: backlight.Response):
    """Print backlight on status"""
    log_dbg("backlight", f"On: {response.backlight_on}")


def handle_response_backlight_off(response: backlight.Response):
    """Print backlight off status"""
    log_dbg("backlight", f"Off: {response.backlight_off}")


def handle_response_backlight_toggle(response: backlight.Response):
    """Print backlight toggle status"""
    log_dbg("backlight", f"Toggle: {response.backlight_toggle}")


def handle_response_backlight_is_on(response: backlight.Response):
    """Print backlight is on status"""
    log_dbg("backlight", f"Backlight state: {response.backlight_is_on}")


def handle_response_backlight_get_brightness(response: backlight.Response):
    """Print backlight brightness"""
    log_dbg("backlight", f"Brightness: {response.backlight_get_brightness}")


def handle_response_backlight_set_brightness(response: backlight.Response):
    """Print backlight brightness"""
    log_dbg("backlight", f"Set brightness: {response.backlight_set_brightness}")

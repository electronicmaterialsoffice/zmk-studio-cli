# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""haptics Response handler"""

from ....logger import log_dbg
from ....proto import haptics_pb2 as haptics


def handle_response(response: haptics.Response):
    """Handle behaviors Response from ZMK Studio RPC Protocol"""
    response_type = response.WhichOneof("response_type")
    if response_type == "haptics_on":
        handle_response_haptics_on(response=response)
    if response_type == "haptics_off":
        handle_response_haptics_off(response=response)
    if response_type == "haptics_toggle":
        handle_response_haptics_toggle(response=response)
    if response_type == "haptics_is_on":
        handle_response_haptics_is_on(response=response)
    if response_type == "haptics_get_rated_voltage":
        handle_response_haptics_get_rated_voltage(response=response)
    if response_type == "haptics_set_rated_voltage":
        handle_response_haptics_set_rated_voltage(response=response)


def handle_response_haptics_on(response: haptics.Response):
    """Print haptics on status"""
    log_dbg("haptics", f"On: {response.haptics_on}")


def handle_response_haptics_off(response: haptics.Response):
    """Print haptics off status"""
    log_dbg("haptics", f"Off: {response.haptics_off}")


def handle_response_haptics_toggle(response: haptics.Response):
    """Print haptics toggle status"""
    log_dbg("haptics", f"Toggle: {response.haptics_toggle}")


def handle_response_haptics_is_on(response: haptics.Response):
    """Print haptics is on status"""
    log_dbg("haptics", f"Haptics state: {response.haptics_is_on}")


def handle_response_haptics_get_rated_voltage(response: haptics.Response):
    """Print haptics rated voltage"""
    log_dbg("haptics", f"Rated Voltage: {response.haptics_get_rated_voltage}")


def handle_response_haptics_set_rated_voltage(response: haptics.Response):
    """Print haptics rated voltage"""
    log_dbg("haptics", f"Set rated voltage: {response.haptics_set_rated_voltage}")

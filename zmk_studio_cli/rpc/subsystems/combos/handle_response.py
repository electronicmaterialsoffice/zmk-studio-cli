# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""combos Response handler"""

from ....logger import log_dbg
from ....proto import combos_pb2 as combos


def handle_response(response: combos.Response):
    """Handle combos Response from ZMK Studio RPC Protocol"""
    response_type = response.WhichOneof("response_type")
    if response_type == "get_combos":
        handle_response_get_combos(response=response)
    elif response_type == "add_combo":
        handle_response_add_combo(response=response)
    elif response_type == "delete_combo":
        handle_response_delete_combo(response=response)
    elif response_type == "set_combo_layer_state":
        handle_response_set_combo_layer_state(response=response)
    elif response_type == "set_combo_position_state":
        handle_response_set_combo_position_state(response=response)
    elif response_type == "set_combo_binding":
        handle_response_set_combo_binding(response=response)
    elif response_type == "set_combo_timeout":
        handle_response_set_combo_timeout(response=response)
    elif response_type == "set_combo_slow_release_state":
        handle_response_set_combo_slow_release_state(response=response)
    else:
        log_wrn("combos", "Unhandled combos response type")

def handle_response_get_combos(response: combos.Response):
    """Print behavior details"""
    combos = response.get_combos
    log_dbg("combos", combos)

def handle_response_add_combo(response: combos.Response):
    """Print add combo response"""
    combo = response.add_combo
    log_dbg("combos", combo)

def handle_response_delete_combo(response: combos.Response):
    """Print delete combo response"""
    res = response.delete_combo
    log_dbg("combos", res)

def handle_response_set_combo_layer_state(response: combos.Response):
    """Print set combo layer state response"""
    res = response.set_combo_layer_state
    log_dbg("combos", res)

def handle_response_set_combo_position_state(response: combos.Response):
    """Print set combo position state response"""
    res = response.set_combo_position_state
    log_dbg("combos", res)

def handle_response_set_combo_timeout(response: combos.Response):
    """Print set combo position state response"""
    res = response.set_combo_timeout
    log_dbg("combos", res)

def handle_response_set_combo_binding(response: combos.Response):
    """Print set combo position state response"""
    res = response.set_combo_binding
    log_dbg("combos", res)

def handle_response_set_combo_slow_release_state(response: combos.Response):
    """Print set combo slow-reease state response"""
    res = response.set_combo_slow_release_state
    log_dbg("combos", res)

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""sensors Response handler"""

from ....logger import log_dbg
from ....proto import sensors_pb2 as sensors
from .error_conditions import RESP_SET_SENSOR_BINDING, RESP_SET_SENSOR_CONFIG


def handle_response(response: sensors.Response):
    """Handle behaviors Response from ZMK Studio RPC Protocol"""
    response_type = response.WhichOneof("response_type")
    if response_type == "get_sensor_binding":
        handle_response_get_sensor_binding(response=response)
    if response_type == "set_sensor_binding":
        handle_response_set_sensor_binding(response=response)
    if response_type == "get_sensor_config":
        handle_response_get_sensor_config(response=response)
    if response_type == "set_sensor_config":
        handle_response_set_sensor_config(response=response)


def handle_response_get_sensor_binding(response: sensors.Response):
    """Print sensor binding details"""
    computed_behavior_id = response.get_sensor_binding.computed_behavior_id
    behavior_id = response.get_sensor_binding.behavior_id
    param1 = response.get_sensor_binding.param1
    param2 = response.get_sensor_binding.param2
    log_dbg("sensors", f"Behavior ID (Computed): {computed_behavior_id}")
    log_dbg("sensors", f"Behavior ID (Current): {behavior_id}")
    log_dbg("sensors", f"Parameter 1: {hex(param1)}")
    log_dbg("sensors", f"Parameter 2: {hex(param2)}")


def handle_response_set_sensor_binding(response: sensors.Response):
    """Print set sensor binding details"""
    set_sensor_binding_resp = response.set_sensor_binding
    log_dbg("sensors", "Set sensor binding:")
    log_dbg("sensors", RESP_SET_SENSOR_BINDING[set_sensor_binding_resp])


def handle_response_get_sensor_config(response: sensors.Response):
    """Print sensor config"""
    triggers_per_rotation = response.get_sensor_config.triggers_per_rotation
    log_dbg("sensors", f"triggers_per_rotation: {triggers_per_rotation}")


def handle_response_set_sensor_config(response: sensors.Response):
    """Print set sensor config details"""
    set_sensor_config_resp = response.set_sensor_config
    log_dbg("sensors", "Set sensor config:")
    log_dbg("sensors", RESP_SET_SENSOR_CONFIG[set_sensor_config_resp])

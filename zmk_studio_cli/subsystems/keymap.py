# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT

import serial
from ..proto import studio_pb2 as studio
from ..rpc import send_request, get_response, handle_response


def get_keymap(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 1
    request.keymap.get_keymap = True

    send_request(ser, request)
    handle_response(get_response(ser, verbose))
    


class BehaviorBinding:
    def __init__(self, behavior_id, param1, param2):
        self._behavior_id = behavior_id
        self._param1 = param1
        self._param2 = param2

    @property
    def behavior_id(self):
        return self._behavior_id

    @property
    def param1(self):
        return self._param1

    @property
    def param2(self):
        return self._param2


def set_layer_binding(
    ser: serial.Serial,
    layer_id: int | None,
    key_position: int | None,
    behavior: BehaviorBinding,
    verbose: bool,
):
    request = studio.Request()
    request.request_id = 2
    request.keymap.set_layer_binding.layer_id = layer_id
    request.keymap.set_layer_binding.key_position = key_position
    request.keymap.set_layer_binding.binding.behavior_id = behavior.behavior_id
    request.keymap.set_layer_binding.binding.param1 = behavior.param1
    request.keymap.set_layer_binding.binding.param2 = behavior.param2

    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def check_unsaved_changes(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 3
    request.keymap.check_unsaved_changes = True

    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def save_changes(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 4
    request.keymap.save_changes = True

    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def discard_changes(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 5
    request.keymap.discard_changes = True

    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def get_physical_layouts(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 6
    request.keymap.get_physical_layouts = True

    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def set_active_physical_layout(ser: serial.Serial, layout: int | None, verbose: bool):
    request = studio.Request()
    request.request_id = 7
    request.keymap.set_active_physical_layout = layout

    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def move_layer(
    ser: serial.Serial, start_index: int | None, dest_index: int | None, verbose: bool
):
    request = studio.Request()
    request.request_id = 8
    request.keymap.move_layer.start_index = start_index
    request.keymap.move_layer.dest_index = dest_index

    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def add_layer(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 9
    request.keymap.add_layer.SetInParent()

    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def remove_layer(ser: serial.Serial, layer_index: int | None, verbose: bool):
    request = studio.Request()
    request.request_id = 10
    request.keymap.remove_layer.layer_index = layer_index

    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def restore_layer(
    ser: serial.Serial, layer_id: int | None, at_index: int | None, verbose: bool
):
    request = studio.Request()
    request.request_id = 11
    request.keymap.restore_layer.layer_id = layer_id
    request.keymap.restore_layer.at_index = at_index

    send_request(ser, request)
    handle_response(get_response(ser, verbose))


def set_layer_props(
    ser: serial.Serial, layer_id: int | None, name: str | None, verbose: bool
):
    request = studio.Request()
    request.request_id = 12
    request.keymap.set_layer_props.layer_id = layer_id
    request.keymap.set_layer_props.name = name

    send_request(ser, request)
    handle_response(get_response(ser, verbose))

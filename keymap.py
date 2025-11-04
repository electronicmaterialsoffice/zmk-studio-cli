import serial
import proto.studio_pb2 as studio_pb2
import rpc


def get_keymap(ser: serial.Serial):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.get_keymap = True
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


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
    ser: serial.Serial, layer_id: int, key_position: int, behavior: BehaviorBinding
):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.set_layer_binding.layer_id = layer_id
    request.keymap.set_layer_binding.key_position = key_position
    request.keymap.set_layer_binding.binding.behavior_id = behavior.behavior_id
    request.keymap.set_layer_binding.binding.param1 = behavior.param1
    request.keymap.set_layer_binding.binding.param2 = behavior.param2
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def check_unsaved_changes(ser: serial.Serial):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.check_unsaved_changes = True
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def save_changes(ser: serial.Serial):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.save_changes = True
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def discard_changes(ser: serial.Serial):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.discard_changes = True
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def get_physical_layouts(ser: serial.Serial):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.get_physical_layouts = True
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def set_active_physical_layout(ser: serial.Serial, layout: int):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.set_active_physical_layout = layout
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def move_layer(ser: serial.Serial, start_index: int, dest_index: int):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.move_layer.start_index = start_index
    request.keymap.move_layer.dest_index = dest_index
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


# Todo: review add layer
def add_layer(ser: serial.Serial):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.add_layer = True
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def remove_layer(ser: serial.Serial, layer_index: int):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.remove_layer.layer_index = layer_index
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def restore_layer(ser: serial.Serial, layer_id: int, at_index: int):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.restore_layer.layer_id = layer_id
    request.keymap.restore_layer.at_index = at_index
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def set_layer_props(ser: serial.Serial, layer_id: int, name: str):
    request = studio_pb2.Request()
    request.request_id = 1
    request.keymap.set_layer_props.layer_id = layer_id
    request.keymap.set_layer_props.name = name
    rpc.send_request(ser, request)
    rpc.handle_response(ser)

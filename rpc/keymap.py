import serial
import proto.studio_pb2 as studio
import rpc.rpc as rpc

SaveChangesErrorCode = ["OK", "GENERIC", "NOT_SUPPORTED", "NO_SPACE"]
SetLayerBindingResponse = [
    "OK",
    "INVALID_LOCATION",
    "INVALID_BEHAVIOR",
    "INVALID_PARAMETERS",
]
MoveLayerErrorCode = ["OK", "GENERIC", "INVALID_LAYER", "INVALID_DESTINATION"]
AddLayerErrorCode = ["OK", "GENERIC", "NO_SPACE"]
RemoveLayerErrorCode = ["OK", "GENERIC", "INVALID_INDEX"]
RestoreLayerErrorCode = ["OK", "GENERIC", "INVALID_ID", "INVALID_INDEX"]
SetLayerPropsResponse = ["OK", "GENERIC", "INVALID_ID"]
SetActivePhysicalLayoutErrorCode = ["OK", "GENERIC", "INVALID_LAYOUT_INDEX"]


def get_keymap(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 1
    request.keymap.get_keymap = True

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


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
    layer_id: int,
    key_position: int,
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

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


def check_unsaved_changes(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 3
    request.keymap.check_unsaved_changes = True

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


def save_changes(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 4
    request.keymap.save_changes = True

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


def discard_changes(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 5
    request.keymap.discard_changes = True

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


def get_physical_layouts(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 6
    request.keymap.get_physical_layouts = True

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


def set_active_physical_layout(ser: serial.Serial, layout: int, verbose: bool):
    request = studio.Request()
    request.request_id = 7
    request.keymap.set_active_physical_layout = layout

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


def move_layer(ser: serial.Serial, start_index: int, dest_index: int, verbose: bool):
    request = studio.Request()
    request.request_id = 8
    request.keymap.move_layer.start_index = start_index
    request.keymap.move_layer.dest_index = dest_index

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


def add_layer(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 9
    request.keymap.add_layer.SetInParent()

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


def remove_layer(ser: serial.Serial, layer_index: int, verbose: bool):
    request = studio.Request()
    request.request_id = 10
    request.keymap.remove_layer.layer_index = layer_index

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


def restore_layer(ser: serial.Serial, layer_id: int, at_index: int, verbose: bool):
    request = studio.Request()
    request.request_id = 11
    request.keymap.restore_layer.layer_id = layer_id
    request.keymap.restore_layer.at_index = at_index

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


def set_layer_props(ser: serial.Serial, layer_id: int, name: str, verbose: bool):
    request = studio.Request()
    request.request_id = 12
    request.keymap.set_layer_props.layer_id = layer_id
    request.keymap.set_layer_props.name = name

    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)

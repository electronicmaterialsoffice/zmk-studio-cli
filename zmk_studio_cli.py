import argparse
import serial

import requests.core as core
import requests.behaviors as behaviors
import requests.keymap as keymap
from requests.keymap import BehaviorBinding


def zmk_studio_cli(args):
    ser = serial.Serial(args.port)
    verbose = args.verbose

    if args.get_device_info:
        core.get_device_info(ser, verbose)
        return
    if args.get_lock_state:
        core.get_lock_state(ser, verbose)
        return
    if args.lock:
        core.lock(ser, verbose)
        return
    if args.reset_settings:
        core.reset_settings(ser, verbose)
        return

    if args.list_all_behaviors:
        behaviors.list_all_behaviors(ser, verbose)
        return
    if args.get_behavior_details:
        assert args.behavior_id != None
        behavior_id = args.behavior_id
        behaviors.get_behavior_details(ser, behavior_id, verbose)
        return

    if args.get_keymap:
        keymap.get_keymap(ser, verbose)
        return
    if args.set_layer_binding:
        assert args.layer_id != None
        assert args.key_position != None
        assert args.behavior_id != None

        layer_id = args.layer_id
        key_position = args.key_position
        behavior_id = args.behavior_id
        param1 = args.param1 if args.param1 else 0
        param2 = args.param2 if args.param2 else 0
        behavior = BehaviorBinding(behavior_id, param1, param2)
        keymap.set_layer_binding(ser, layer_id, key_position, behavior, verbose)
        return
    if args.check_unsaved_changes:
        keymap.check_unsaved_changes(ser, verbose)
        return
    if args.save_changes:
        keymap.save_changes(ser, verbose)
        return
    if args.discard_changes:
        keymap.discard_changes(ser, verbose)
        return
    if args.get_physical_layouts:
        keymap.get_physical_layouts(ser, verbose)
        return
    if args.set_active_physical_layout != None:
        layout = args.set_active_physical_layout
        keymap.set_active_physical_layout(ser, layout, verbose)
        return
    if args.move_layer:
        assert args.start_index != None
        assert args.dest_index != None
        start_index = args.start_index
        dest_index = args.dest_index
        keymap.move_layer(ser, start_index, dest_index, bool)
        return
    if args.add_layer:
        keymap.add_layer(ser, verbose)
        return
    if args.remove_layer:
        assert args.layer_index != None
        layer_index = args.layer_index
        keymap.remove_layer(ser, layer_index, bool)
        return
    if args.restore_layer:
        assert args.layer_id != None
        assert args.layer_index != None
        layer_id = args.layer_id
        layer_index = args.layer_index
        keymap.restore_layer(ser, layer_id, layer_index, verbose)
        return
    if args.set_layer_props:
        assert args.layer_id != None
        assert args.name != None

        layer_id = args.layer_id
        name = args.name

        keymap.set_layer_props(ser, layer_id, name, verbose)
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("-p", "--port", type=str, required=True, help="Serial Port")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose printing"
    )

    # Common Arguments
    parser.add_argument("-l", "--layer-index", type=int, help="Layer index")
    parser.add_argument("-li", "--layer-id", type=int, help="Layer ID")
    parser.add_argument("-kp", "--key-position", type=int, help="Key position")
    parser.add_argument("-b", "--behavior-id", type=int, help="Behavior ID")
    parser.add_argument("-p1", "--param1", type=int, help="Behavior param1")
    parser.add_argument("-p2", "--param2", type=int, help="Behavior param2")
    parser.add_argument("-n", "--name", type=str, help="Layer name")
    parser.add_argument("-start", "--start-index", type=int, help="Layer move start")
    parser.add_argument("-dest", "--dest-index", type=int, help="Layer move dest")

    # Core Arguments
    parser.add_argument(
        "--get-device-info", action="store_true", help="core: Get device info"
    )
    parser.add_argument(
        "--get-lock-state", action="store_true", help="core: Get lock state"
    )
    parser.add_argument("--lock", action="store_true", help="core: Lock keyboard")
    parser.add_argument(
        "--reset-settings", action="store_true", help="core: Reset settings"
    )

    # Behavior Arguments
    parser.add_argument(
        "--list-all-behaviors",
        action="store_true",
        help="behaviors: List all behaviors",
    )
    parser.add_argument(
        "--get-behavior-details",
        action="store_true",
        help="behaviors: Get behavior details",
    )

    # Keymap Arguments
    parser.add_argument("--get-keymap", action="store_true", help="keymap: Get keymap")
    parser.add_argument(
        "--set-layer-binding", action="store_true", help="keymap: Set layer binding"
    )
    parser.add_argument(
        "--check-unsaved-changes",
        action="store_true",
        help="keymap: Check unsaved changes",
    )
    parser.add_argument(
        "--save-changes", action="store_true", help="keymap: Save changes"
    )
    parser.add_argument(
        "--discard-changes", action="store_true", help="keymap: Discard changes"
    )
    parser.add_argument(
        "--get-physical-layouts",
        action="store_true",
        help="keymap: Get physical layouts",
    )
    parser.add_argument(
        "--set-active-physical-layout",
        type=int,
        help="keymap: Set active physical layout",
    )
    parser.add_argument("--move-layer", action="store_true", help="keymap: Move layer")
    parser.add_argument("--add-layer", action="store_true", help="keymap: Add layer")
    parser.add_argument(
        "--remove-layer", action="store_true", help="keymap: Remove layer"
    )
    parser.add_argument(
        "--restore-layer", action="store_true", help="keymap: Restore layer"
    )
    parser.add_argument(
        "--set-layer-props", action="store_true", help="keymap: Set layer properties"
    )

    args = parser.parse_args()

    zmk_studio_cli(args)

import serial
import proto.studio_pb2 as studio_pb2

RPC_SOF = b"\xab"
RPC_ESC = b"\xac"
RPC_EOF = b"\xad"

simple_errors = [
    "GENERIC",
    "UNLOCK_REQUIRED",
    "RPC_NOT_FOUND",
    "MSG_DECODE_FAILED",
    "MSG_ENCODE_FAILED",
]

lock_state_strings = ["LOCKED", "UNLOCKED"]


def send_request(ser: serial.Serial, request: bytes):
    ser.write(RPC_SOF)
    ser.write(request.SerializeToString())
    ser.write(RPC_EOF)


def handle_response(ser: serial.Serial, verbose: bool):
    response_msg = b""
    response_chr = ser.read()
    if response_chr == RPC_SOF:
        while True:
            response_chr = ser.read()
            if response_chr == RPC_ESC:
                response_chr = ser.read()
                response_msg = response_msg + response_chr
                continue
            if response_chr == RPC_EOF:
                break
            response_msg = response_msg + response_chr

    if verbose:
        print(response_msg)

    response = studio_pb2.Response()
    notification = studio_pb2.Notification()
    try:
        response.ParseFromString(response_msg)
    except Exception as error:
        print("An exception occurred: ", error)
        return

    response_type = response.WhichOneof("type")

    if response_type == "request_response":
        req_response = response.request_response
        req_response_subsystem = req_response.WhichOneof("subsystem")

        if req_response_subsystem == "meta":
            meta_response_type = req_response.meta.WhichOneof("response_type")
            if meta_response_type == "no_response":
                print("<meta> NO RESPONSE")
                return
            if meta_response_type == "simple_error":
                simple_error_index = req_response.meta.simple_error
                print(f"<meta> SIMPLE ERROR: {simple_errors[simple_error_index]}")
                return

        if req_response_subsystem == "core":
            core_response_type = req_response.core.WhichOneof("response_type")
            if core_response_type == "get_device_info":
                device_info = req_response.core.get_device_info
                print(f"<core> Device Name: {device_info.name}")
                print(f"<core>    Serial #: {device_info.serial_number}")
                return
            if core_response_type == "get_lock_state":
                lock_state = req_response.core.get_lock_state
                print(f"<core> LOCK STATE: {lock_state_strings[lock_state]}")
                return
            if core_response_type == "reset_settings":
                print(f"<core> Reset settings: {req_response.core.reset_settings}")
                return

        if req_response_subsystem == "behaviors":
            behaviors_response_type = req_response.behaviors.WhichOneof("response_type")
            if behaviors_response_type == "list_all_behaviors":
                print("<behaviors> Listing all behaviors...")
                print(req_response.behaviors.list_all_behaviors.behaviors)
                return
            if behaviors_response_type == "get_behavior_details":
                behavior_id = req_response.behaviors.get_behavior_details.id
                behavior_display_name = (
                    req_response.behaviors.get_behavior_details.display_name
                )
                behavior_metadata = req_response.behaviors.get_behavior_details.metadata
                print(f"<behaviors> Behavior ID: {behavior_id}")
                print(f"<behaviors> Display Name: {behavior_display_name}")
                if len(behavior_metadata) > 0:
                    print(f"<behaviors> Metadata:")
                    print(behavior_metadata)
                return

        if req_response_subsystem == "keymap":
            keymap_response_type = req_response.keymap.WhichOneof("response_type")
            if keymap_response_type == "get_keymap":
                keymap = req_response.keymap.get_keymap
                print(keymap)
                return
            if keymap_response_type == "set_layer_binding":
                set_layer_binding = req_response.keymap.set_layer_binding
                set_layer_binding_strings = [
                    "OK",
                    "INVALID_LOCATION",
                    "INVALID_BEHAVIOR",
                    "INVALID_PARAMETERS",
                ]
                print(
                    f"<keymap> Set layer binding: {set_layer_binding_strings[set_layer_binding]}"
                )
                return
            if keymap_response_type == "check_unsaved_changes":
                unsaved_changes = req_response.keymap.check_unsaved_changes
                print(f"<keymap> Check unsaved changes: {unsaved_changes}")
                return
            if keymap_response_type == "save_changes":
                saved_changes_ok = req_response.keymap.save_changes.ok
                saved_changes_err = req_response.keymap.save_changes.err
                saved_changes_err_strings = [
                    "OK",
                    "GENERIC",
                    "NOT_SUPPORTED",
                    "NO_SPACE",
                ]
                print(f"<keymap> Saved changes? {saved_changes_ok}")
                if saved_changes_err:
                    print(
                        f"<keymap> Saved changes err: {saved_changes_err_strings[saved_changes_err]}"
                    )
                return
            if keymap_response_type == "discard_changes":
                discard_changes = req_response.keymap.discard_changes
                print(f"<keymap> Discarded changes? {discard_changes}")
                return
            if keymap_response_type == "get_physical_layouts":
                physical_layouts = req_response.keymap.get_physical_layouts
                print(physical_layouts)
                return
            if keymap_response_type == "set_active_physical_layout":
                set_active_physical_layout_response_ok = (
                    req_response.keymap.set_active_physical_layout.ok
                )
                set_active_physical_layout_response_err = (
                    req_response.keymap.set_active_physical_layout.err
                )
                print(
                    f"<keymap> Set active physical layout? {set_active_physical_layout_response_ok}"
                )
                if set_active_physical_layout_response_err:
                    print(
                        f"<keymap> Set active physical layout err: {set_active_physical_layout_response_err}"
                    )
                return
            if keymap_response_type == "move_layer":
                print("move_layer")
                return
            if keymap_response_type == "add_layer":
                print("add_layer")
                return
            if keymap_response_type == "remove_layer":
                print("remove_layer")
                return
            if keymap_response_type == "restore_layer":
                print("restore_layer")
                restore_layer_response_ok = req_response.keymap.restore_layer.ok
                restore_layer_response_err = req_response.keymap.restore_layer.err
                print(f"<keymap> Restore layer? {restore_layer_response_ok}")
                if set_active_physical_layout_response_err:
                    print(f"<keymap> Restore layer err: {restore_layer_response_err}")
                return
            if keymap_response_type == "set_layer_props":
                print(
                    f"<keymap> Set_layer_props? {req_response.keymap.set_layer_props}"
                )
                return
            return

        print("<err> Invalid RequestResponse subsystem.")
        return

    if response_type == "notification":
        notification = response.notification
        notification_subsystem = notification.WhichOneof("subsystem")

        if notification_subsystem == "core":
            core_notification_type = notification.core.WhichOneof("notification_type")
            if core_notification_type == "lock_state_changed":
                lock_state = notification.core.lock_state_changed
                print(f"<core, notif> LOCK STATE: {lock_state_strings[lock_state]}")
                return
            print("<err> Invalid notification type")
            return

        if notification_subsystem == "keymap":
            keymap_notification_type = notification.keymap.WhichOneof(
                "notification_type"
            )
            if keymap_notification_type == "unsaved_changes_status_changed":
                unsaved_changes_status_changed = (
                    notification.keymap.unsaved_changes_status_changed
                )
                print(
                    f"<keymap, notif> Unsaved changes status changed: {unsaved_changes_status_changed}"
                )
                return
            print("<err> Invalid notification type")
            return

        print("<err> Invalid notification subsystem.")
        return

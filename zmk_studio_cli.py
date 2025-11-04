import serial
import core
import behaviors
import keymap
from keymap import BehaviorBinding

ZMK_STUDIO_CLI_CORE = True
ZMK_STUDIO_CLI_BEHAVIORS = False
ZMK_STUDIO_CLI_KEYMAP = True


def main():
    ser = serial.Serial("COM7")

    if ZMK_STUDIO_CLI_CORE:
        core.get_device_info(ser)
        print("")
        core.get_lock_state(ser)
        print("")
        core.lock(ser)
        print("")
        core.get_lock_state(ser)
        print("")
        core.reset_settings(ser)
        print("")

    if ZMK_STUDIO_CLI_BEHAVIORS:
        behaviors.list_all_behaviors(ser)
        print("")
        behaviors.get_behavior_details(ser, 14)
        print("")
        behaviors.get_behavior_details(ser, 1)
        print("")
        behaviors.get_behavior_details(ser, 4)
        print("")
        behaviors.get_behavior_details(ser, 15)
        print("")
        behaviors.get_behavior_details(ser, 16)
        print("")
        behaviors.get_behavior_details(ser, 17)
        print("")
        behaviors.get_behavior_details(ser, 6)
        print("")
        behaviors.get_behavior_details(ser, 18)
        print("")
        behaviors.get_behavior_details(ser, 19)
        print("")
        behaviors.get_behavior_details(ser, 21)
        print("")
        behaviors.get_behavior_details(ser, 22)
        print("")
        behaviors.get_behavior_details(ser, 2)
        print("")
        behaviors.get_behavior_details(ser, 12)
        print("")
        behaviors.get_behavior_details(ser, 23)
        print("")
        behaviors.get_behavior_details(ser, 3)
        print("")
        behaviors.get_behavior_details(ser, 7)
        print("")
        behaviors.get_behavior_details(ser, 8)
        print("")
        behaviors.get_behavior_details(ser, 26)
        print("")
        behaviors.get_behavior_details(ser, 9)
        print("")
        behaviors.get_behavior_details(ser, 27)
        print("")
        behaviors.get_behavior_details(ser, 5)
        print("")
        behaviors.get_behavior_details(ser, 24)
        print("")
        behaviors.get_behavior_details(ser, 31)
        print("")
        behaviors.get_behavior_details(ser, 32)
        print("")
        behaviors.get_behavior_details(ser, 33)
        print("")
        behaviors.get_behavior_details(ser, 36)
        print("")
        behaviors.get_behavior_details(ser, 20)
        print("")
        behaviors.get_behavior_details(ser, 28)
        print("")
        behaviors.get_behavior_details(ser, 35)
        print("")
        behaviors.get_behavior_details(ser, 10)
        print("")
        behaviors.get_behavior_details(ser, 11)
        print("")
        behaviors.get_behavior_details(ser, 30)
        print("")
        behaviors.get_behavior_details(ser, 13)
        print("")

    if ZMK_STUDIO_CLI_KEYMAP:
        keymap.get_keymap(ser)
        print("")
        keymap.save_changes(ser)
        print("")
        BSPC = BehaviorBinding(4, 458756, 0)

        keymap.set_layer_binding(ser, 0, 0, BSPC)
        keymap.get_keymap(ser)


try:
    main()
except Exception as error:
    print(error)

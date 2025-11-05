import serial
import proto.studio_pb2 as studio
import rpc.rpc as rpc


def list_all_behaviors(ser: serial.Serial, verbose: bool):
    request = studio.Request()
    request.request_id = 1
    request.behaviors.list_all_behaviors = True
    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)


def get_behavior_details(ser: serial.Serial, behavior_id: int, verbose: bool):
    request = studio.Request()
    request.request_id = 2
    request.behaviors.get_behavior_details.behavior_id = behavior_id
    rpc.send_request(ser, request)
    rpc.handle_response(ser, verbose)

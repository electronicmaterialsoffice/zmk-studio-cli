import serial
import proto.studio_pb2 as studio_pb2
import rpc


def get_device_info(ser: serial.Serial):
    request = studio_pb2.Request()
    request.request_id = 1
    request.core.get_device_info = True
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def get_lock_state(ser: serial.Serial):
    request = studio_pb2.Request()
    request.request_id = 1
    request.core.get_lock_state = True
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def lock(ser: serial.Serial):
    request = studio_pb2.Request()
    request.request_id = 1
    request.core.lock = True
    rpc.send_request(ser, request)
    rpc.handle_response(ser)


def reset_settings(ser: serial.Serial):
    request = studio_pb2.Request()
    request.request_id = 1
    request.core.reset_settings = True
    rpc.send_request(ser, request)
    rpc.handle_response(ser)

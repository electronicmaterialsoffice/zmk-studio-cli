# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio sensors RPC handlers"""

from ....proto import sensors_pb2 as sensors
from .handle_notification import handle_notification
from .handle_response import handle_response


def handle_request_response_sensors(request_response: sensors.Response):
    """Handle RequestResponse of type sensors"""
    handle_response(request_response)


def handle_notification_sensors(notification: sensors.Response):
    """Handle Notification of type sensors"""
    handle_notification(notification)

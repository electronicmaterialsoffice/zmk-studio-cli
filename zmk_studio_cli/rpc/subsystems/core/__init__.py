# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio core RPC handlers"""

from ....proto import studio_pb2 as studio
from .handle_notification import handle_notification
from .handle_response import handle_response


def handle_request_response_core(request_response: studio.RequestResponse.core):
    """Handle RequestResponse of type core"""
    handle_response(request_response)


def handle_notification_core(notification: studio.RequestResponse.core):
    """Handle Notification of type core"""
    handle_notification(notification)

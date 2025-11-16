# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio core RPC handlers"""

from ....proto import core_pb2 as core
from .handle_notification import handle_notification
from .handle_response import handle_response


def handle_request_response_core(request_response: core.Response):
    """Handle RequestResponse of type core"""
    handle_response(request_response)


def handle_notification_core(notification: core.Response):
    """Handle Notification of type core"""
    handle_notification(notification)

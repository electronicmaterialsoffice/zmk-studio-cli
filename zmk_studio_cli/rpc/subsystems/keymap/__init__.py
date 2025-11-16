# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio keymap RPC handlers"""

from .handle_response import handle_response
from .handle_notification import handle_notification
from ....proto import studio_pb2 as studio


def handle_request_response_keymap(request_response: studio.RequestResponse.keymap):
    """Handle RequestResponse of type keymap"""
    handle_response(request_response)


def handle_notification_keymap(notification: studio.RequestResponse.keymap):
    """Handle Notification of type keymap"""
    handle_notification(notification)

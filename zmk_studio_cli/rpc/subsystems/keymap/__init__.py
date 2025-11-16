# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio keymap RPC handlers"""

from ....proto import studio_pb2 as studio
from .handle_notification import handle_notification
from .handle_response import handle_response


def handle_request_response_keymap(request_response: studio.RequestResponse.keymap):
    """Handle RequestResponse of type keymap"""
    handle_response(request_response)


def handle_notification_keymap(notification: studio.RequestResponse.keymap):
    """Handle Notification of type keymap"""
    handle_notification(notification)

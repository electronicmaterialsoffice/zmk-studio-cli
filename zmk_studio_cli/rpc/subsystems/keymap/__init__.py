# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio keymap RPC handlers"""

from ....proto import keymap_pb2 as keymap
from .handle_notification import handle_notification
from .handle_response import handle_response


def handle_request_response_keymap(request_response: keymap.Response):
    """Handle RequestResponse of type keymap"""
    handle_response(request_response)


def handle_notification_keymap(notification: keymap.Response):
    """Handle Notification of type keymap"""
    handle_notification(notification)

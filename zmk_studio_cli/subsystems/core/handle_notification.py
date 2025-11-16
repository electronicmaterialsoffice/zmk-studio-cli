# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""core Notification handler"""

from .lockstate import LOCKSTATE
from ...logger import log_notif
from ...proto import core_pb2 as core


def handle_notification(notification: core.Notification):
    """Handle core Notification from ZMK Studio RPC Protocol"""
    notification_type = notification.WhichOneof("notification_type")
    if notification_type == "lock_state_changed":
        handle_notification_lock_state_changed(notification=notification)


def handle_notification_lock_state_changed(notification: core.Notification):
    """Print lock state changed notification"""
    lock_state = notification.lock_state_changed
    log_notif("core", f"LOCK STATE: {LOCKSTATE[lock_state]}")

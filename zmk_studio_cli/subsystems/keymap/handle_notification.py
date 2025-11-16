# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""keymap Notification handler"""

from ...logger import log_notif
from ...proto import keymap_pb2 as keymap


def handle_notification(notification: keymap.Notification):
    """Handle keymap Notification from ZMK Studio RPC Protocol"""
    notification_type = notification.WhichOneof("notification_type")
    if notification_type == "unsaved_changes_status_changed":
        handle_notification_unsaved_changes_status_changed(notification=notification)


def handle_notification_unsaved_changes_status_changed(
    notification: keymap.Notification,
):
    """Print unsaved changes status changed notification"""
    unsaved_changes_status_changed = notification.unsaved_changes_status_changed
    log_notif(
        "keymap",
        "Unsaved changes status changed:",
        unsaved_changes_status_changed,
    )

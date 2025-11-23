# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""sensors Notification handler"""

from ....logger import log_notif
from ....proto import sensors_pb2 as sensors


def handle_notification(notification: sensors.Notification):
    """Handle sensors Notification from ZMK Studio RPC Protocol"""
    notification_type = notification.WhichOneof("notification_type")
    if notification_type == "unsaved_changes_status_changed":
        handle_notification_unsaved_changes_status_changed(notification=notification)


def handle_notification_unsaved_changes_status_changed(
    notification: sensors.Notification,
):
    """Print unsaved changes status changed notification"""
    unsaved_changes_status_changed = notification.unsaved_changes_status_changed
    log_notif(
        "sensors",
        "Unsaved changes status changed:",
        unsaved_changes_status_changed,
    )

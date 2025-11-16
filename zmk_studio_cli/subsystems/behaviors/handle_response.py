# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""behaviors Response handler"""

from ...logger import log_dbg
from ...proto import behaviors_pb2 as behaviors


def handle_response(response: behaviors.Response):
    """Handle behaviors Response from ZMK Studio RPC Protocol"""
    response_type = response.WhichOneof("response_type")
    if response_type == "list_all_behaviors":
        # Deprecated: handled externally
        #     log_dbg("behaviors", "Listing all behaviors...")
        #     log_dbg("behaviors", request_response_behaviors.list_all_behaviors.behaviors)
        return
    if response_type == "get_behavior_details":
        handle_response_get_behavior_details(response=response)


def handle_response_get_behavior_details(response: behaviors.Response):
    """Print behavior details"""
    behavior_id = response.get_behavior_details.id
    behavior_display_name = response.get_behavior_details.display_name
    behavior_metadata = response.get_behavior_details.metadata
    log_dbg("behaviors", f"Behavior ID: {behavior_id}")
    log_dbg("behaviors", f"Display Name: {behavior_display_name}")
    if len(behavior_metadata) > 0:
        log_dbg("behaviors", "Metadata:\n", behavior_metadata)

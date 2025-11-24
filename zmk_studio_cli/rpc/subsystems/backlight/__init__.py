# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio backlight RPC handlers"""

from ....proto import backlight_pb2 as backlight
from .handle_response import handle_response


def handle_request_response_backlight(request_response: backlight.Response):
    """Handle RequestResponse of type backlight"""
    handle_response(request_response)

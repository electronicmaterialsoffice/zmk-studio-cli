# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio haptics RPC handlers"""

from ....proto import haptics_pb2 as haptics
from .handle_response import handle_response


def handle_request_response_haptics(request_response: haptics.Response):
    """Handle RequestResponse of type haptics"""
    handle_response(request_response)

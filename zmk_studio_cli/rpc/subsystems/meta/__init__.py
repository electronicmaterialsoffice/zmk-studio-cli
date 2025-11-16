# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio meta RPC handlers"""

from .handle_response import handle_response
from ....proto import studio_pb2 as studio


def handle_request_response_meta(request_response: studio.RequestResponse.meta):
    """Handle RequestResponse of type meta"""
    handle_response(request_response)

# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio behaviors RPC handlers"""

from .handle_response import handle_response
from ....proto import studio_pb2 as studio


def handle_request_response_behaviors(
    request_response: studio.RequestResponse.behaviors,
):
    """Handle RequestResponse of type behaviors"""
    handle_response(request_response)

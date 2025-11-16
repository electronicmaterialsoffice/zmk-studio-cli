# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio behaviors RPC handlers"""

from ....proto import studio_pb2 as studio
from .handle_response import handle_response


def handle_request_response_behaviors(
    request_response: studio.RequestResponse.behaviors,
):
    """Handle RequestResponse of type behaviors"""
    handle_response(request_response)

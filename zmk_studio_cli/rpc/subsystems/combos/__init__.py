# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio combos RPC handlers"""

from ....proto import combos_pb2 as combos
from .handle_response import handle_response


def handle_request_response_combos(request_response: combos.Response):
    """Handle RequestResponse of type behaviors"""
    handle_response(request_response)

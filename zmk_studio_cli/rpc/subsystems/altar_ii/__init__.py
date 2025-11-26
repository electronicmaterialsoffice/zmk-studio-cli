# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio Altar II RPC handlers"""

from ....proto import altar_ii_pb2 as altar_ii
from .handle_response import handle_response


def handle_request_response_altar_ii(request_response: altar_ii.Response):
    """Handle RequestResponse of type altar_ii"""
    handle_response(request_response)

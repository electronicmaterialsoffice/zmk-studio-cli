# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""ZMK Studio meta RPC handlers"""

from ....proto import meta_pb2 as meta
from .handle_response import handle_response


def handle_request_response_meta(request_response: meta.Response):
    """Handle RequestResponse of type meta"""
    handle_response(request_response)

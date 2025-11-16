# Copyright (c) 2025 The ZMK Contributors
# SPDX-License-Identifier: MIT
"""meta Response handler"""

from .error_conditions import ERROR_CONDITIONS
from ....logger import log_err
from ....proto import meta_pb2 as meta


def handle_response(response: meta.Response):
    """Handle meta Response from ZMK Studio RPC Protocol"""
    response_type = response.WhichOneof("response_type")
    if response_type == "no_response":
        return
    if response_type == "simple_error":
        handle_response_simple_error(response=response)


def handle_response_simple_error(response: meta.Response):
    """Print simple error response"""
    simple_error_index = response.simple_error
    log_err("meta", ERROR_CONDITIONS[simple_error_index])

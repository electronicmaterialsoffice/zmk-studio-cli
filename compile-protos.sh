#!/bin/bash

protoc --proto_path="zmk-studio-messages/proto/zmk" --python_out="zmk_studio_cli/proto/" zmk-studio-messages/proto/zmk/*.proto
fix-protobuf-imports zmk_studio_cli/proto
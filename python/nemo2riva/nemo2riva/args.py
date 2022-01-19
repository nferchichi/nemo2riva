# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

import argparse
from distutils.util import strtobool


def get_args(argv):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=f"Convert NeMo models to Riva EFF input format",
    )
    parser.add_argument("source", help="Source .nemo file")
    parser.add_argument("--out", default=None, help="Location to write resulting Riva EFF input to")
    parser.add_argument("--validate", action="store_true", help="Validate using schemas")
    parser.add_argument("--runtime-check", action="store_true", help="Runtime check of exported net result")
    parser.add_argument("--schema", default=None, help="Schema file to use for validation")
    parser.add_argument("--format", default=None, help="Force specific export format: ONNX|TS|CKPT")
    parser.add_argument("--verbose", default=None, help="Verbose level for logging")
    parser.add_argument("--key", default=None, help="Encryption key or file, default is None")
    parser.add_argument(
        "--autocast",
        type=lambda x: bool(strtobool(x)),
        default=None,
        help="Override autocast in the schema : True|False",
    )
    parser.add_argument("--max-batch", type=int, default=None, help="Max batch size for model export")
    parser.add_argument("--max-dim", type=int, default=None, help="Max dimension(s) for model export")
    parser.add_argument("--onnx-opset", type=int, default=None, help="ONNX opset for model export")

    args = parser.parse_args(argv)
    return args

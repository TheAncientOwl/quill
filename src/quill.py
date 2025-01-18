#!/bin/python3
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file quill.py
#  @author Alexandru Delegeanu
#  @version 0.1
#  @description Entry point of Quill toolkit manager
#

import os

from quill.configs.quill_config import QuillConfig
from quill.logic.args_manager import ArgsManager


def main():
    quill_config = QuillConfig()
    args_manager = ArgsManager()


if __name__ == "__main__":
    main()

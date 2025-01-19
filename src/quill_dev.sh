#!/bin/bash
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file quill_dev.sh
#  @author Alexandru Delegeanu
#  @version 0.1
#  @description Clean, Install, Run dev server
#

set -e

root_path=$(pwd)

quill.py --clean
cd $root_path

quill.py --install
cd $root_path

quill_run_server.sh

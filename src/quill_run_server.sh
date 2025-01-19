#!/bin/bash
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file quill_run_server.sh
#  @author Alexandru Delegeanu
#  @version 0.1
#  @description Script to run development server in linux environment
#

set -e

root_path=$(pwd)

quill.py --pre-dev-server-run

cd $(pwd)/dev/server
echo $(pwd)
./start.sh

cd $root_path

quill.py --post-dev-server-run

#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file process.py
#  @author Alexandru Delegeanu
#  @version 0.2
#  @description Process utilities
#

import os
import sys
import subprocess


class Process:
    def run_command_process(command, action_on_fail_exit=None, exit_on_fail: bool = True, cwd=os.getcwd()) -> int:
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd)

        for line in process.stdout:
            print(line, end="")

        process.wait()

        if exit_on_fail == True and process.returncode != 0:
            if action_on_fail_exit != None:
                action_on_fail_exit()
            sys.exit(process.returncode)

        return process.returncode

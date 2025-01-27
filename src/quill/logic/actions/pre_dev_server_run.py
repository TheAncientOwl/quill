#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file pre_dev_server_run.py
#  @author Alexandru Delegeanu
#  @version 0.2
#  @description Run configured pre-server-run commands
#

import os
import sys
import shutil
import argparse

from quill.common.logger import Logger
from quill.configs.project_config import ProjectConfig
from quill.logic.project_paths import ProjectPaths
from quill.utils.process import Process


class PreDevServerRun(argparse._StoreTrueAction):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)

        Logger.info("[Running] pre-server-run commands")

        project_paths = ProjectPaths()
        project_config = ProjectConfig()

        commands = project_config.get_pre_server_run_commands()

        for command in commands:
            if len(commands) != 0:
                final_command = [
                    part.replace("$PROJECT_ROOT", project_paths.get_project_root_path())
                    for part in command
                ]
                if command != final_command:
                    Logger.info(f"[Running] {command} =~ {final_command}")
                else:
                    Logger.info(f"[Running] {command}")
                Process.run_command_process(final_command)
                Logger.info(f"[Done] {command}")

        Logger.info("[Done] pre-server-run commands")

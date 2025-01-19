#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file install.py
#  @author Alexandru Delegeanu
#  @version 0.2
#  @description Compile the plugin and install it to the dev server
#

import os
import sys
import shutil
import argparse

from quill.common.logger import Logger
from quill.configs.project_config import ProjectConfig
from quill.logic.project_paths import ProjectPaths
from quill.utils.process import Process


class Install(argparse._StoreTrueAction):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)

        Logger.info("Verbose: OFF")
        paths = ProjectPaths()
        project_config = ProjectConfig()

        def clear():
            tmp_path = paths.get_feather_toolkit_tmp_path()
            if os.path.exists(tmp_path):
                shutil.rmtree(tmp_path)

        Process.run_command_process(
            command=project_config.get_install_command(), action_on_exit=clear, cwd=paths.get_project_root_path())

        Logger.info(f"Plugin installed to {paths.get_server_plugins_path()}")

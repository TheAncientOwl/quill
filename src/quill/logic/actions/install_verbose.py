#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file install_verbose.py
#  @author Alexandru Delegeanu
#  @version 0.3
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


class InstallVerbose(argparse._StoreTrueAction):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)

        Logger.info("Verbose: ON")
        paths = ProjectPaths()

        project_config = ProjectConfig()

        def clear():
            tmp_path = paths.get_feather_toolkit_tmp_path()
            if os.path.exists(tmp_path):
                shutil.rmtree(tmp_path)

        Process.run_command_process(
            command=project_config.get_install_command(), action_on_exit=clear, cwd=paths.get_project_root_path())

        project_name = project_config.get_project_name()

        src = paths.get_target_path()
        dst = paths.get_server_plugins_path()

        for file_name in os.listdir(src):
            if file_name.endswith('.jar') and file_name.startswith(project_name):
                src_file = os.path.join(src, file_name)
                dst_file = os.path.join(dst, file_name)

                shutil.copy2(src_file, dst_file)

        Logger.info(f"Plugin installed to {paths.get_server_plugins_path()}")

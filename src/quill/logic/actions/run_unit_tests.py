#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file run_unit_tests.py
#  @author Alexandru Delegeanu
#  @version 0.4
#  @description Run unit tests
#

import os
import sys
import shutil
import argparse

from quill.common.logger import Logger
from quill.configs.project_config import ProjectConfig
from quill.logic.project_paths import ProjectPaths
from quill.utils.process import Process


class RunUnitTests(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super().__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)

        if values != None:
            Logger.info(f"Running unit tests for: {values}")

        project_config = ProjectConfig()

        project_paths = ProjectPaths()

        def clear():
            tmp_path = project_paths.get_feather_toolkit_tmp_path()
            print(f"Clean {tmp_path}")
            if os.path.exists(tmp_path):
                shutil.rmtree(tmp_path)

        if values == None:
            Process.run_command_process(
                project_config.get_test_all_command(), action_on_fail_exit=clear
            )
        else:
            package = RunUnitTests.convert_path_to_package(values)

            cmd = (
                project_config.get_test_file_command()
                if package.endswith(".java")
                else project_config.get_test_package_command()
            )

            command = [arg.replace("$TEST_NAME", package) for arg in cmd]

            Process.run_command_process(command, action_on_fail_exit=clear)

        clear()

    #
    # @brief Convert a file path to a package name by:
    #        - Removing the "src/test/java/" prefix.
    #        - Replacing "/" with ".".
    #
    # @param path(str): The file path to convert.
    # @return str The corresponding package name.
    #
    def convert_path_to_package(path: str) -> str:
        if path.endswith("/"):
            path = path[:-1]

        if path.startswith("src/test/java/"):
            path = path[len("src/test/java/") :]

        return path.replace("/", ".")

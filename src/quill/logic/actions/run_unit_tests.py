#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file run_unit_tests.py
#  @author Alexandru Delegeanu
#  @version 0.1
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

        if values == None:
            Process.run_command_process(project_config.get_test_all_command())
        else:
            package = RunUnitTests.convert_path_to_package(values)

            command = [arg.replace("$TEST_NAME", package)
                       for arg in project_config.get_test_package_command()]

            Process.run_command_process(command)

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

        if path.endswith(".java"):
            path = path[:-5]

        if path.startswith("src/test/java/"):
            path = path[len("src/test/java/"):]

        return path.replace("/", ".")

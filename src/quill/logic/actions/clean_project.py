#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file clean_project.py
#  @author Alexandru Delegeanu
#  @version 0.3
#  @description Run unit tests coverage
#

import re
import os
import sys
import shutil
import argparse

from quill.common.logger import Logger
from quill.configs.project_config import ProjectConfig
from quill.logic.project_paths import ProjectPaths
from quill.utils.process import Process


class CleanProject(argparse._StoreTrueAction):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)

        project_paths = ProjectPaths()
        project_config = ProjectConfig()

        clean_paths = []

        clean_path_regex = re.compile(r"^(.*)/(.*)$")

        for path in project_config.get_clean_paths_list():
            match = re.match(clean_path_regex, path)

            Logger.info(f"Checking \"{path}\"")

            if match:
                parent_path = os.path.join(
                    project_paths.get_project_root_path(), match.group(1))
                entry_regex = re.compile(match.group(2))

                for entry in os.listdir(parent_path):
                    if not re.match(entry_regex, entry):
                        continue

                    entry_path = os.path.join(parent_path, entry)

                    if os.path.isfile(entry_path):
                        os.remove(entry_path)
                        Logger.info(f"Removed {entry_path}")
                    elif os.path.isdir(entry_path):
                        shutil.rmtree(entry_path)
                        Logger.info(f"Removed {entry_path}")

            else:
                absolute_path = os.path.join(
                    project_paths.get_project_root_path(), path)
                Logger.warn(f"{absolute_path} is not valid directory path")

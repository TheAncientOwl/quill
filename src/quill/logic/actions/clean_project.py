#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file clean_project.py
#  @author Alexandru Delegeanu
#  @version 0.1
#  @description Run unit tests coverage
#

import os
import sys
import shutil
import argparse

from quill.common.logger import Logger
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

        plugins_path = project_paths.get_server_plugins_path()
        Logger.info(f"Removing FeatherCore files from {plugins_path}")
        removed = False
        for entry in os.listdir(plugins_path):
            if not entry.startswith("FeatherCore"):
                continue

            path = os.path.join(plugins_path, entry)

            if os.path.isfile(path):
                os.remove(path)
                removed = True
                Logger.info(f"Removed {path}")
            elif os.path.isdir(path):
                removed = True
                shutil.rmtree(path)
                Logger.info(f"Removed {path}")

        if removed == False:
            Logger.info(f"No FeatherCore files to remove at {plugins_path}")

        target_path = project_paths.get_target_path()
        Logger.info(f"Removing {target_path}")
        if os.path.exists(target_path):
            shutil.rmtree(target_path)
            Logger.info(f"Removed {target_path}")
        else:
            Logger.info(f"No target files to remove at {target_path}")

#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file configure_action.py
#  @author Alexandru Delegeanu
#  @version 0.3
#  @description Configure maven project
#

import os
import sys
import shutil
import argparse

from quill.common.logger import Logger
from quill.configs.project_config import ProjectConfig
from quill.logic.project_paths import ProjectPaths
from quill.utils.process import Process


class Configure(argparse._StoreTrueAction):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)

        Logger.info("Configuring project based on pom.xml")

        project_config = ProjectConfig()

        Process.run_command_process(project_config.get_configure_clean_command())

        Process.run_command_process(project_config.get_configure_eclipse_command())

        Logger.info("Configuration done")

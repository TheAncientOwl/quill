#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file code_coverage.py
#  @author Alexandru Delegeanu
#  @version 0.2
#  @description Run unit tests coverage
#

import os
import sys
import shutil
import argparse

from quill.common.logger import Logger
from quill.configs.project_config import ProjectConfig
from quill.logic.project_paths import ProjectPaths
from quill.utils.process import Process


class CodeCoverage(argparse._StoreTrueAction):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)

        Logger.info("Running unit tests coverage")

        project_config = ProjectConfig()

        Process.run_command_process(project_config.get_coverage_command())

        paths = ProjectPaths()
        jacoco_index_html = os.path.join(paths.get_jacoco_path(), "index.html")

        Logger.info(f"Coverage finished, report location: {jacoco_index_html}")

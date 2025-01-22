#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file code_coverage.py
#  @author Alexandru Delegeanu
#  @version 0.5
#  @description Run unit tests coverage
#

import os
import sys
import shutil
import argparse
import pathlib

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
        project_paths = ProjectPaths()

        def clear():
            tmp_path = project_paths.get_feather_toolkit_tmp_path()
            print(f"Clean {tmp_path}")
            if os.path.exists(tmp_path):
                shutil.rmtree(tmp_path)

        Process.run_command_process(
            project_config.get_coverage_command(), action_on_fail_exit=clear)

        clear()

        paths = ProjectPaths()
        jacoco_index_html = os.path.join(paths.get_jacoco_path(), "index.html")

        config_resources_path = project_config.get_coverage_resources_list_path()
        if len(config_resources_path) != 0:
            resources_to_add_path = paths.get_project_root_path()
            for path_part in config_resources_path:
                resources_to_add_path = os.path.join(
                    resources_to_add_path, path_part)

            if not os.path.exists(resources_to_add_path):
                Logger.err(
                    f"Resources path does not exist {resources_to_add_path}")
                sys.exit(1)

            if not os.path.isdir(resources_to_add_path):
                Logger.err(f"{resources_to_add_path} is not a directory")
                sys.exit(1)

            src_path = pathlib.Path(resources_to_add_path)
            dst_path = pathlib.Path(paths.get_jacoco_resources_path())

            for item in src_path.iterdir():
                src_item = src_path / item.name
                dst_item = dst_path / item.name

                if src_item.is_dir():
                    shutil.copytree(src_item, dst_item)
                else:
                    shutil.copy2(src_item, dst_item)

        Logger.info(f"Coverage finished, report location: {jacoco_index_html}")

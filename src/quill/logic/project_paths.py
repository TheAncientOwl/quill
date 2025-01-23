#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file project_paths.py
#  @author Alexandru Delegeanu
#  @version 0.3
#  @description Lightweight utility to get project paths
#

import os

from quill.common.logger import Logger


class ProjectPaths:
    def load_env_project_root(warn_when_toolkit_root_not_set: bool):
        project_root = os.getenv(
            "FEATHER_TOOLKIT_PROJECT_ROOT")

        if project_root == None:
            project_root = os.getcwd()
            if warn_when_toolkit_root_not_set:
                Logger.warn(
                    "FEATHER_TOOLKIT_PROJECT_ROOT env variable was not set, using " + project_root)

        return project_root

    def __init__(self, project_root: str = load_env_project_root(False)):
        self._project_root = project_root

    def get_project_root_path(self) -> str:
        return self._project_root

    def get_server_path(self) -> str:
        return os.path.join(self._project_root, "dev", "server")

    def get_server_plugins_path(self) -> str:
        return os.path.join(self.get_server_path(), "plugins")

    def get_feather_toolkit_tmp_path(self):
        return os.path.join(os.path.expanduser("~"), "tmp-feather-toolkit")

    def get_target_path(self):
        return os.path.join(self._project_root, "target")

    def get_jacoco_path(self):
        return os.path.join(self.get_target_path(), "site", "jacoco")

    def get_feather_toolkit_path(self):
        return os.path.join(self._project_root, "feather-toolkit")

    def get_feather_toolkit_config_path(self):
        return os.path.join(self.get_feather_toolkit_path(), "config.json")

    def get_jacoco_resources_path(self):
        return os.path.join(self.get_jacoco_path(), "jacoco-resources")

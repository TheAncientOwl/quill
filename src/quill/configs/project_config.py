#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file project_config.py
#  @author Alexandru Delegeanu
#  @version 0.1
#  @description Configuration of Feather toolkit project
#  @see project/templates/configs/feather-toolkit-config.json
#

import sys
import json

from quill.common.logger import Logger
from quill.common.singleton import singleton
from quill.logic.project_paths import ProjectPaths


@singleton
class ProjectConfig:
    def __init__(self):
        project_paths = ProjectPaths()

        with open(project_paths.get_feather_toolkit_config_path(), "r") as config_file:
            self._json_config = json.load(config_file)

    def get_java_file_header(self):
        self.assert_key_exists("headers", self._json_config)
        self.assert_key_exists("java", self._json_config["headers"])

        return self._json_config["headers"]["java"]

    def get_java_test_file_header(self):
        self.assert_key_exists("headers", self._json_config)
        self.assert_key_exists("java-test", self._json_config["headers"])

        return self._json_config["headers"]["java-test"][:]

    def assert_key_exists(self, key, json_obj):
        if key not in json_obj:
            project_paths = ProjectPaths()
            formatted_json = json.dumps(json_obj, indent=4)
            Logger.err(
                f"Missing config \"{key}\" key from \"{formatted_json}\" ({project_paths.get_feather_toolkit_config_path()})")
            sys.exit(1)

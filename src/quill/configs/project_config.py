#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file project_config.py
#  @author Alexandru Delegeanu
#  @version 0.3
#  @description Configuration of Feather toolkit project
#  @see project/templates/configs/feather-toolkit-config.linux.json
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

    def assert_key_exists(self, key, json_obj):
        if key not in json_obj:
            project_paths = ProjectPaths()
            formatted_json = json.dumps(json_obj, indent=4)
            Logger.err(
                f"Missing config \"{key}\" key from \"{formatted_json}\" ({project_paths.get_feather_toolkit_config_path()})")
            sys.exit(1)

    def get_java_file_header(self):
        self.assert_key_exists("headers", self._json_config)
        self.assert_key_exists("java", self._json_config["headers"])

        return self._json_config["headers"]["java"]

    def get_java_test_file_header(self):
        self.assert_key_exists("headers", self._json_config)
        self.assert_key_exists("java-test", self._json_config["headers"])

        return self._json_config["headers"]["java-test"][:]

    def get_coverage_command(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists("coverage", self._json_config["commands"])

        return self._json_config["commands"]["coverage"]

    def get_install_command(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists("install", self._json_config["commands"])

        return self._json_config["commands"]["install"]

    def get_install_verbose_command(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists(
            "install-verbose", self._json_config["commands"])

        return self._json_config["commands"]["install-verbose"]

    def get_configure_clean_command(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists("configure", self._json_config["commands"])
        self.assert_key_exists(
            "clean", self._json_config["commands"]["configure"])

        return self._json_config["commands"]["configure"]["clean"]

    def get_configure_eclipse_command(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists("configure", self._json_config["commands"])
        self.assert_key_exists(
            "eclipse", self._json_config["commands"]["configure"])

        return self._json_config["commands"]["configure"]["eclipse"]

    def get_coverage_resources_list_path(self):
        self.assert_key_exists("coverage-resources-path", self._json_config)

        return self._json_config["coverage-resources-path"]

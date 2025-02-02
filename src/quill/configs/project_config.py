#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file project_config.py
#  @author Alexandru Delegeanu
#  @version 0.9
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

        with open(project_paths.get_quill_config_path(), "r") as config_file:
            self._json_config = json.load(config_file)

    def assert_key_exists(self, key, json_obj):
        if key not in json_obj:
            project_paths = ProjectPaths()
            formatted_json = json.dumps(json_obj, indent=4)
            Logger.error(
                f'Missing config "{key}" key from "{formatted_json}" ({project_paths.get_quill_config_path()})'
            )
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
        self.assert_key_exists("install-verbose", self._json_config["commands"])

        return self._json_config["commands"]["install-verbose"]

    def get_configure_clean_command(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists("configure", self._json_config["commands"])
        self.assert_key_exists("clean", self._json_config["commands"]["configure"])

        return self._json_config["commands"]["configure"]["clean"]

    def get_configure_eclipse_command(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists("configure", self._json_config["commands"])
        self.assert_key_exists("eclipse", self._json_config["commands"]["configure"])

        return self._json_config["commands"]["configure"]["eclipse"]

    def get_coverage_resources_list_path(self):
        self.assert_key_exists("coverage-resources-path", self._json_config)

        return self._json_config["coverage-resources-path"]

    def get_test_all_command(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists("test", self._json_config["commands"])
        self.assert_key_exists("all", self._json_config["commands"]["test"])

        return self._json_config["commands"]["test"]["all"]

    def get_test_package_command(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists("test", self._json_config["commands"])
        self.assert_key_exists("package", self._json_config["commands"]["test"])

        return self._json_config["commands"]["test"]["package"]

    def get_test_file_command(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists("test", self._json_config["commands"])
        self.assert_key_exists("file", self._json_config["commands"]["test"])

        return self._json_config["commands"]["test"]["file"]

    def get_pre_server_run_commands(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists("run", self._json_config["commands"])
        self.assert_key_exists("pre", self._json_config["commands"]["run"])

        return self._json_config["commands"]["run"]["pre"]

    def get_post_server_run_commands(self):
        self.assert_key_exists("commands", self._json_config)
        self.assert_key_exists("run", self._json_config["commands"])
        self.assert_key_exists("post", self._json_config["commands"]["run"])

        return self._json_config["commands"]["run"]["post"]

    def get_project_name(self):
        self.assert_key_exists("project", self._json_config)

        return self._json_config["project"]

    def get_clean_paths_list(self):
        self.assert_key_exists("clean-paths", self._json_config)

        return self._json_config["clean-paths"]

#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file configure_headers.py
#  @author Alexandru Delegeanu
#  @version 0.4
#  @description Add headers to new files
#

import os
import sys
import shutil
import argparse

from quill.common.logger import Logger
from quill.configs.project_config import ProjectConfig
from quill.logic.project_paths import ProjectPaths
from quill.utils.process import Process


class JavaFilePaths:
    def __init__(self, java=[], java_test=[]):
        self.java_test = java_test
        self.java = java


class ConfigureHeaders(argparse._StoreTrueAction):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)

        Logger.info("Configuring file headers")

        project_paths = ProjectPaths()
        project_config = ProjectConfig()

        java_files = ConfigureHeaders.get_all_java_files(
            project_paths.get_project_root_path()
        )

        headers_count = 0

        headers_count = headers_count + ConfigureHeaders.add_headers(
            java_files.java, project_config.get_java_file_header()
        )
        headers_count = headers_count + ConfigureHeaders.add_headers(
            java_files.java_test, project_config.get_java_test_file_header()
        )

        if headers_count == 0:
            Logger.info("No file headers to configure")
        else:
            Logger.info(
                "Configured "
                + str(headers_count)
                + " file header"
                + ("" if headers_count == 1 else "s")
            )

    def get_all_java_files(path: str) -> JavaFilePaths:
        java_test_files = []
        java_files = []

        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith("Test.java"):
                    java_test_files.append(os.path.join(root, file))
                elif file.endswith(".java"):
                    java_files.append(os.path.join(root, file))

        return JavaFilePaths(java=java_files, java_test=java_test_files)

    def add_headers(files=[], header=[]):
        headers_count = 0

        if len(header) == 0:
            return headers_count

        for file_path in files:
            content = None
            try:
                with open(file_path, "r") as file:
                    content = file.readlines()
            except Exception as e:
                Logger.error(f"Error processing {file_path}: {e}")
                sys.exit(1)

            if len(content) == 0 or content[0][:-1] == header[0]:
                continue

            headers_count = headers_count + 1

            file_header = []

            file_name = os.path.basename(file_path)
            non_test_base_file_name = (
                file_name[:-9] if file_name.endswith("Test.java") else None
            )

            for header_line in header:
                new_line = header_line + "\n"
                new_line = new_line.replace("$FILE_NAME", file_name)
                if non_test_base_file_name != None:
                    new_line = new_line.replace(
                        "$NON_TEST_BASE_FILE_NAME", non_test_base_file_name
                    )

                file_header.append(new_line)

            updated_content = file_header + content

            with open(file_path, "w") as file:
                file.writelines(updated_content)

            Logger.info(f"Header added to {file_path}")

        return headers_count

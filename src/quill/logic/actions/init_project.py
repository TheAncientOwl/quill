#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file init_project.py
#  @author Alexandru Delegeanu
#  @version 0.2
#  @description Setup new FeatherToolkit project
#

import os
import sys
import shutil
import argparse

from quill.common.logger import Logger
from quill.configs.project_config import ProjectConfig
from quill.logic.project_paths import ProjectPaths
from quill.utils.process import Process


def get_env_var(var_name):
    value = os.environ.get(var_name)
    if value is None:
        raise EnvironmentError(
            f"Environment variable '{
                               var_name}' is not set."
        )
    return value


class InitProject(argparse._StoreTrueAction):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)

        Logger.info("Init project")

        # 1. Fetch project variables
        group_id = input("Enter the group ID (e.g., com.example): ").strip()
        project_name = input("Enter the Project Name (no spaces): ").strip()
        artifact_id = project_name.lower()
        group_id = f"{group_id}.{artifact_id}"

        # 2. Setup project files
        QUILL_HOME = get_env_var("QUILL_HOME")

        QUILL_PROJECT_TEMPLATES = os.path.join(QUILL_HOME, "project", "templates")

        # TODO: ask for toolkit & paper versions
        placeholders = {
            "$TOOLKIT_PACKAGE": group_id,
            "$TOOLKIT_GROUP_ID": group_id,
            "$TOOLKIT_ARTIFACT_ID": artifact_id,
            "$TOOLKIT_PROJECT_NAME": project_name,
            "$TOOLKIT_PROJECT_VERSION": "v1.0.0",
            "$TOOLKIT_VERSION": "v1.0.1",
            "$TOOLKIT_PAPER_VERSION": "1.21.3-R0.1-SNAPSHOT",
        }

        # 2.1. Copy boilerplate
        QUILL_NEW_PROJECT_TEMPLATE = os.path.join(
            QUILL_PROJECT_TEMPLATES, "new-project"
        )

        for entry in os.listdir(QUILL_NEW_PROJECT_TEMPLATE):
            src = os.path.join(QUILL_NEW_PROJECT_TEMPLATE, entry)
            dst = os.path.join(os.getcwd(), entry)

            Logger.info(f"Copy {src} -> {dst}")

            if os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dst)

        # 2.2. Move dev.java.TOOLKIT_PACKAGE to group_id
        shutil.move(
            os.path.join(os.getcwd(), "src", "main", "java", "TOOLKIT_PACKAGE"),
            os.path.join(
                os.getcwd(), "src", "main", "java", group_id.replace(".", os.sep)
            ),
        )
        shutil.move(
            os.path.join(os.getcwd(), "src", "test", "java", "TOOLKIT_PACKAGE"),
            os.path.join(
                os.getcwd(), "src", "test", "java", group_id.replace(".", os.sep)
            ),
        )

        # 2.3. Setup placeholders
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if (
                    file.endswith(".java")
                    or file.endswith(".xml")
                    or file.endswith(".yml")
                ):
                    path = os.path.join(root, file)
                    Logger.info(f"Setup {path} placeholders")
                    InitProject.replace_placeholders(path, placeholders)

        # 2.4. Move EntryPoint
        entry_point_path = os.path.join(
            os.getcwd(), "src", "main", "java", group_id.replace(".", os.sep), "core"
        )
        shutil.move(
            os.path.join(entry_point_path, "$TOOLKIT_PROJECT_NAME.java"),
            os.path.join(entry_point_path, f"{project_name}.java"),
        )

        # 3. Add quill.json
        local_quill_json = os.path.join(os.getcwd(), "quill.json")
        shutil.copy2(
            os.path.join(
                QUILL_PROJECT_TEMPLATES, "configs", "feather-toolkit-config.linux.json"
            ),
            local_quill_json,
        )
        InitProject.replace_placeholders(local_quill_json, placeholders)

    def replace_placeholders(file_path, placeholders):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            for placeholder, value in placeholders.items():
                content = content.replace(placeholder, value)

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
        except FileNotFoundError:
            Logger.error(f"{file_path} does not exist")
        except Exception as e:
            Logger.error(f"An error ocurred: {e}")

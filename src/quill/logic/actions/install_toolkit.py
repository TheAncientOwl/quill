#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file install_toolkit.py
#  @author Alexandru Delegeanu
#  @version 0.2
#  @description Compile the plugin and install it to the dev server
#

import os
import sys
import shutil
import argparse
import requests

from quill.common.logger import Logger
from quill.configs.project_config import ProjectConfig
from quill.logic.project_paths import ProjectPaths
from quill.utils.process import Process


class InstallToolkit(argparse._StoreAction):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)

        version = values

        Logger.info(f"Trying to install FeatherToolkit-{version}...")

        tmp_path = os.path.join(os.path.expanduser("~"), ".quill-install-tmp")

        def clear():
            if os.path.exists(tmp_path):
                shutil.rmtree(tmp_path)

        clear()

        os.mkdir(tmp_path)

        feather_toolkit_github_url = f"https://github.com/TheAncientOwl/feather-toolkit/releases/download/{
            version}/FeatherToolkit-{version}.jar"
        feather_toolkit_jar = os.path.join(
            tmp_path, f"FeatherToolkit-{version}.jar")

        try:
            with requests.get(feather_toolkit_github_url, stream=True) as response:
                response.raise_for_status()

                with open(feather_toolkit_jar, 'wb') as file:
                    shutil.copyfileobj(response.raw, file)

            Logger.info(f'Downloaded FeatherCore-{version}.jar')

        except requests.exceptions.HTTPError as e:
            # For 404, 403, 500 errors, etc.
            Logger.error(f'HTTP error occurred: {e}')
            clear()
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            # For other request-related issues
            Logger.error(f'Request error occurred: {e}')
            clear()
            sys.exit(1)
        except Exception as e:
            # For other unexpected errors (e.g., file write errors)
            Logger.error(f'An error occurred: {e}')
            clear()
            sys.exit(1)

        group_id = "dev.defaultybuf.feather.toolkit"
        artifact_id = "FeatherToolkit"

        Process.run_command_process(
            command=[
                "mvn", "install:install-file", f"-Dfile={feather_toolkit_jar}", f"-DgroupId={group_id}", f"-DartifactId={artifact_id}", f"-Dversion={version}", "-Dpackaging=jar"],
            action_on_fail_exit=clear)

        clear()

        Logger.info(f"Installed FeatherToolkit-{version}")
        Logger.info(f"Group ID: {group_id}")
        Logger.info(f"Artifact ID: {artifact_id}")
        Logger.info(f"Version: {version}")

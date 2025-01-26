#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file args_manager.py
#  @author Alexandru Delegeanu
#  @version 0.12
#  @description Arguments manager of Quill toolkit manager
#

import argparse
import sys

from colorama import Fore as Color
from quill.common.logger import Logger

import quill.logic.actions as actions


class ColoredHelpFormatter(argparse.HelpFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.colors = [Color.LIGHTWHITE_EX, Color.WHITE]
        self.current_color_index = 0

    def _format_action(self, action):
        color = self.colors[self.current_color_index]
        self.current_color_index = (
            self.current_color_index + 1) % len(self.colors)

        action_help = super()._format_action(action)
        return f"{color}{action_help}{Color.RESET}"


class ArgsManager:
    def __init__(self):
        self._parser = argparse.ArgumentParser(
            prog=f"Quill",
            description=f"{
                Color.WHITE}Feather Toolkit manager utility{Color.RESET}",
            formatter_class=ColoredHelpFormatter
        )

        # TODO: Fetch version from config
        self._parser.add_argument(
            "-v",
            "--version",
            action="version",
            version="%(prog)s v1.0.0"
        )
        self._parser.add_argument(
            "-c",
            "--clean",
            action=actions.CleanProject,
            help="remove the plugin files from dev server location and target files"
        )
        self._parser.add_argument(
            "-i",
            "--install",
            action=actions.InstallProject,
            help="compile the plugin and install it to the dev server"
        )
        self._parser.add_argument(
            "-iv",
            "--install-verbose",
            action=actions.InstallProjectVerbose,
            help="verbose output for install command"
        )
        self._parser.add_argument(
            "-x",
            "--configure",
            action=actions.Configure,
            help="configure maven project"
        )
        self._parser.add_argument(
            "-t",
            "--test",
            action=actions.RunUnitTests,
            nargs="?",
            help="run unit tests (default test suite if no specific test is provided)",
            metavar=f"TEST/S"
        )
        self._parser.add_argument(
            "-k",
            "--coverage",
            action=actions.CodeCoverage,
            help="run unit tests coverage"
        )
        self._parser.add_argument(
            "-hh",
            "--headers",
            action=actions.ConfigureHeaders,
            help="configure code files"
        )
        self._parser.add_argument(
            "--pre-dev-server-run",
            action=actions.PreDevServerRun,
            help="run pre-server-run configured commands"
        )
        self._parser.add_argument(
            "--post-dev-server-run",
            action=actions.PostDevServerRun,
            help="run post-server-run configured commands"
        )
        self._parser.add_argument(
            "-it",
            "--install-toolkit",
            nargs=1,
            action=actions.InstallToolkit,
            help=f"install feather toolkit lib",
            metavar=f"VERSION"
        )
        self._parser.add_argument(
            "-rn",
            "--release-notes",
            action=actions.GenerateReleaseNotes,
            help="generate git history between last 2 tags"
        )
        self._parser.add_argument(
            "--init",
            action=actions.InitProject,
            help="initialize feather-toolkit project"
        )

        if len(sys.argv) == 1:
            self._parser.print_help()
            sys.exit(0)

        self._args = self._parser.parse_args()

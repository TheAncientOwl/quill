#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file args_manager.py
#  @author Alexandru Delegeanu
#  @version 0.3
#  @description Arguments manager of Quill toolkit manager
#

import argparse
import sys

from quill.common.logger import Logger

import quill.logic.actions as actions


class ArgsManager:
    def __init__(self):
        self._parser = argparse.ArgumentParser(
            prog="Quill",
            description="Feather Toolkit manager utility"
        )

        self._parser.add_argument(
            "-v",
            "--version",
            action="version",
            version="%(prog)s 0.0.2"
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
            action=actions.Install,
            help="compile the plugin and install it to the dev server"
        )
        self._parser.add_argument(
            "-iv",
            "--install-verbose",
            action=actions.InstallVerbose,
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
            help="run unit tests (default test suite if no specific test is provided)"
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

        if len(sys.argv) == 1:
            self._parser.print_help()
            sys.exit(0)

        self._args = self._parser.parse_args()

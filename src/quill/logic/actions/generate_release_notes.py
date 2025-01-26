#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file generate_release_notes.py
#  @author Alexandru Delegeanu
#  @version 0.1
#  @description Configure maven project
#

import argparse
import subprocess

from quill.common.logger import Logger


class GenerateReleaseNotes(argparse._StoreTrueAction):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)

        last_tag = subprocess.check_output(
            ['git', 'describe', '--tags', '--abbrev=0']).decode('utf-8').strip()

        previous_tag = subprocess.check_output(
            ['git', 'describe', '--tags', '--abbrev=0', f'{last_tag}^']).decode('utf-8').strip()

        Logger.info(f"Last tag: {last_tag}")
        Logger.info(f"Previous tag: {previous_tag}")

        git_log_command = [
            'git', 'log', '--graph', '--pretty=format:%C(auto)%h - %C(bold blue)[%an](https://github.com/%an)%C(reset)%C(auto)%d %C(white)%s%C(reset)',
            '--abbrev-commit', f'{previous_tag}..{last_tag}'
        ]

        git_log = subprocess.check_output(git_log_command).decode('utf-8')

        Logger.info(f"Release notes:\n{git_log}")

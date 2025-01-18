#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file logger.py
#  @author Alexandru Delegeanu
#  @version 0.1
#  @description Logging utility
#

class Logger:
    DARK_RED = "\033[31m"

    DARK_GREEN = "\033[32m"
    YELLOW = "\033[93m"
    DARK_GRAY = "\033[90m"
    LIGHT_GRAY = "\033[37m"
    LIGHT_GREEN = "\033[92m"
    DARK_AQUA = "\033[36m"
    LIGHT_RED = "\033[91m"
    RESET = "\033[0m"

    def info(message: str):
        print(f"[Info] {message}")

    def warn(message: str):
        print(f"[Warning] {message}")

    def err(message: str):
        print(f"[Error] {message}")

    def debug(message: str):
        print(f"[Debug] {message}")

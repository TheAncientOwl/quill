#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file logger.py
#  @author Alexandru Delegeanu
#  @version 0.4
#  @description Logging utility
#

from colorama import Fore as Color


class Logger:
    Color = Color
    BOLD = "\033[1m"
    NORMAL = "\033[0m"

    def log(message: str):
        print(
            f"{Logger.BOLD}{Color.LIGHTBLACK_EX}[{Color.LIGHTYELLOW_EX}Quill"
            f"{Color.LIGHTBLACK_EX}] » {Logger.NORMAL}{Color.RESET}{message}"
        )

    def info(message: str):
        level = Logger.format_level(f"{Color.LIGHTBLUE_EX}Info")
        Logger.log(
            f"{level}{Color.LIGHTBLACK_EX}: "
            f"{Color.LIGHTBLUE_EX}{message}{Color.RESET}"
        )

    def warn(message: str):
        level = Logger.format_level(f"{Color.YELLOW}Warning")
        Logger.log(
            f"{level}{Color.LIGHTBLACK_EX}: {Color.YELLOW}{message}{Color.RESET}"
        )

    def error(message: str):
        level = Logger.format_level(f"{Color.LIGHTRED_EX}Error")
        Logger.log(
            f"{level}{Color.LIGHTBLACK_EX}: {Color.LIGHTRED_EX}{message}{Color.RESET}"
        )

    def debug(message: str):
        level = Logger.format_level(f"{Color.LIGHTGREEN_EX}Debug")
        Logger.log(
            f"{level}{Color.LIGHTBLACK_EX}: {Color.LIGHTGREEN_EX}{message}{Color.RESET}"
        )

    def format_level(level: str):
        return f"{Logger.BOLD}{level}{Logger.NORMAL}{Color.RESET}"


if __name__ == "__main__":
    Logger.info("This is info message")
    Logger.warn("This is warn message")
    Logger.error("This is error message")
    Logger.debug("This is debug message")

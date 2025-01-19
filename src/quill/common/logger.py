#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file logger.py
#  @author Alexandru Delegeanu
#  @version 0.2
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

    def log(message: str):
        print(
            f"{Logger.DARK_GRAY}[{Logger.YELLOW}Quill{Logger.DARK_GRAY}] » {Logger.RESET}{message}")

    def info(message: str):
        Logger.log(
            f"{Logger.DARK_AQUA}Info{Logger.DARK_GRAY}: {Logger.DARK_AQUA}{message}{Logger.RESET}")

    def warn(message: str):
        Logger.log(
            f"{Logger.YELLOW}Warning{Logger.DARK_GRAY}: {Logger.YELLOW}{message}{Logger.RESET}")

    def err(message: str):
        Logger.log(
            f"{Logger.DARK_RED}Error{Logger.DARK_GRAY}: {Logger.LIGHT_RED}{message}{Logger.RESET}")

    def debug(message: str):
        Logger.log(
            f"{Logger.DARK_GREEN}Debug{Logger.DARK_GRAY}: {Logger.LIGHT_GREEN}{message}{Logger.RESET}")


if __name__ == "__main__":
    Logger.info("This is info message")
    Logger.warn("This is warn message")
    Logger.err("This is error message")
    Logger.debug("This is debug message")

#
# -------------------------------------------------------------------------  #
#                        Copyright (c) by Quill 2025                         #
#  ------------------------------------------------------------------------- #
#  @license https://github.com/TheAncientOwl/quill/blob/main/LICENSE
#
#  @file quill_config.py
#  @author Alexandru Delegeanu
#  @version 0.1
#  @description Configuration of Quill toolkit manager
#  @see project/templates/configs/quill-config.json
#

from quill.common.singleton import singleton


@singleton
class QuillConfig:
    def __init__(self):
        pass

    def get_warn_when_toolkit_root_not_set(self):
        return False

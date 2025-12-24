from pathlib import Path
from uuid import uuid4
from platform import system

from .install import WINDOWS_setup, check_install

if not check_install(Path, system):
    WINDOWS_setup


from .cultists import Cultist
from .new_user import new_user





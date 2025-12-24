import platform
from pathlib import Path
from uuid import uuid4

CULTIST_TEMPLATE = {
    "TEMPLATE-4hs834hf74h578fhsmkh23-TEMPLATE": {
        "level": 1,  # -1 = CULTLEADER, 0 = FOLLOWER, 1 = INITIATE
        "experience": {"trees": 0, "bones": 0, "potions": 0},
    }
}

USER_CONFIG_TEMPLATE = {
    "USER-TEMPLATE-4hs834hf74h578fhsmkh23-USER-TEMPLATE": {
        "name": {"first": "Some", "last": "player"},
        "email": "N1oP9@example.com",
        "DATE_TIME_START": 12938.1,}

}

PATHS = {
    "INSTALL": Path(),
    "TEMPLATES": Path(),
    "USER": Path(),
}

def check_install(install_path:Path): 
    tests = [
        install_path.exists(),
        len(list(install_path.glob("*"))) > 0,
    ]
    return all(tests)


def check_user(user_path: Path):
    tests = [
        user_path.exists(),
        len(list(user_path.glob("*"))) > 0,
    ]
    return all(tests)


def new_user():
    id = uuid4()
    name = {
        "first": input("First name: "),
        "last": input("Last name: "),
    }

    TEMPLATE = USER_CONFIG_TEMPLATE.copy()

    TEMPLATE

    return USER_CONFIG_TEMPLATE


def WINDOWS_setup():
    install_path = Path(Path().root) / "Program Files" / "Cultists"
    templates_path = Path(Path().root) / "ProgramData" / "Cultists"
    user_path = Path("~").expanduser() / "AppData" / "Local" / "Cultists"


    ######################### APP INSTALLATION FOLDER
    if not install_path.exists():
        install_path.mkdir(parents=True)
    # TODO: install files to install_path

    ######################### APP TEMPLATES FOLDER
    if not templates_path.exists():
        templates_path.mkdir(parents=True)
    # TODO: save templates to templates_path

    ######################### USER CONFIG FOLDER
    if not user_path.exists():
        user_path.mkdir(parents=True)
    # TODO: save user data to user_path


if __name__ == "__main__":

    PLATFORM_IS_WIN = platform.system() == "Windows"

    if PLATFORM_IS_WIN: WINDOWS_setup()
    else: raise NotImplementedError

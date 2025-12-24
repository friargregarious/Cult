from uuid import uuid4


# individual cultists are stored in json
CULTIST_TEMPLATE = {
    "TEMPLATE-4hs834hf74h578fhsmkh23-TEMPLATE": {
        "level": 1,  # initiate
        "experience": {"trees": 0, "bones": 0, "potions": 0},
    }
}



class Cultist:
    def __init__(self, kwargs:dict):
        if not kwargs: raise ValueError("Cultist object requires **kwargs")
        self.name = kwargs.get("name", str(uuid4()))
        self.level = kwargs.get("level", 1)
        self.experience = kwargs.get("experience", {"trees": 0, "bones": 0, "potions": 0})



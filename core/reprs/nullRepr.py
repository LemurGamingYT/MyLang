from dataclasses import dataclass

@dataclass(init = True, repr = True)
class nullRepr():
    value: str = "null"

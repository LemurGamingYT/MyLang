from dataclasses import dataclass

@dataclass(init = True, repr = True)
class stringRepr():
    value: str

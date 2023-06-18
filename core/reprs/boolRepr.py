from dataclasses import dataclass

@dataclass(init = True, repr = True)
class boolRepr():
    value: bool

from dataclasses import dataclass

@dataclass(init = True, repr = True)
class floatRepr():
    value: float

from dataclasses import dataclass
from typing import Any


@dataclass(init = True, repr = True)
class varRepr():
    name: str
    value: Any
    constant: bool

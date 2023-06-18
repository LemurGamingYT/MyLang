from dataclasses import dataclass

@dataclass(init = True, repr = True)
class intRepr():
    value: int
    
    def __add__(self, other):
        if isinstance(other, intRepr):
            return intRepr(self.value + other.value)
        else:
            # error
            pass

from ..gen.MyLangParser import MyLangParser
from dataclasses import dataclass


@dataclass(init = True, repr = True)
class funcRepr():
    name: str
    parameters: list
    block: MyLangParser.BlockContext

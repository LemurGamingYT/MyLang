from .gen.MyLangVisitor import MyLangVisitor

from .env import Environment

class Visitor(MyLangVisitor):
    def __init__(self) -> None:
        self.env = Environment()

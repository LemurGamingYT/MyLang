from sys import argv

from antlr4 import FileStream, CommonTokenStream

from core.gen.MyLangParser import MyLangParser
from core.gen.MyLangLexer import MyLangLexer
from core.Visitor import Visitor

def Main(f: str):
    code = FileStream(f)
    
    lexer = MyLangLexer(code)
    stream = CommonTokenStream(lexer)
    
    parser = MyLangParser(stream)
    tree = parser.parse()
    
    visitor = Visitor()
    visitor.visit(tree)

if __name__ == "__main__":
    if len(argv) > 1:
        Main(argv[1])
    else:
        Main("examples/test.mylang")

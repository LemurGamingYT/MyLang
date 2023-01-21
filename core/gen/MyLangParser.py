# Generated from core/MyLang.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,47,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,3,2,26,8,
        2,1,2,1,2,1,3,1,3,1,3,5,3,33,8,3,10,3,12,3,36,9,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,3,4,45,8,4,1,4,0,0,5,0,2,4,6,8,0,0,51,0,13,1,0,0,0,
        2,18,1,0,0,0,4,22,1,0,0,0,6,29,1,0,0,0,8,44,1,0,0,0,10,12,3,2,1,
        0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,
        1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,20,3,8,4,0,19,
        21,5,3,0,0,20,19,1,0,0,0,20,21,1,0,0,0,21,3,1,0,0,0,22,23,5,6,0,
        0,23,25,5,1,0,0,24,26,3,6,3,0,25,24,1,0,0,0,25,26,1,0,0,0,26,27,
        1,0,0,0,27,28,5,2,0,0,28,5,1,0,0,0,29,34,3,8,4,0,30,31,5,5,0,0,31,
        33,3,8,4,0,32,30,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,
        0,35,7,1,0,0,0,36,34,1,0,0,0,37,45,5,6,0,0,38,45,5,7,0,0,39,45,5,
        8,0,0,40,45,5,9,0,0,41,45,5,10,0,0,42,45,5,11,0,0,43,45,3,4,2,0,
        44,37,1,0,0,0,44,38,1,0,0,0,44,39,1,0,0,0,44,40,1,0,0,0,44,41,1,
        0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,9,1,0,0,0,5,13,20,25,34,44
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "';'", "'.'", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "SEMI", "DOT", "COMMA", 
                      "ID", "STRING", "INT", "FLOAT", "NULL", "BOOL", "WHITESPACE", 
                      "COMMENT" ]

    RULE_parse = 0
    RULE_stmt = 1
    RULE_call = 2
    RULE_args = 3
    RULE_expr = 4

    ruleNames =  [ "parse", "stmt", "call", "args", "expr" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    SEMI=3
    DOT=4
    COMMA=5
    ID=6
    STRING=7
    INT=8
    FLOAT=9
    NULL=10
    BOOL=11
    WHITESPACE=12
    COMMENT=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MyLangParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StmtContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_parse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = MyLangParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0:
                self.state = 10
                self.stmt()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(MyLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MyLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.expr()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 19
                self.match(MyLangParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(MyLangParser.ArgsContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = MyLangParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(MyLangParser.ID)
            self.state = 23
            self.match(MyLangParser.LPAREN)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0:
                self.state = 24
                self.args()


            self.state = 27
            self.match(MyLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.COMMA)
            else:
                return self.getToken(MyLangParser.COMMA, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = MyLangParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.expr()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 30
                self.match(MyLangParser.COMMA)
                self.state = 31
                self.expr()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MyLangParser.FLOAT, 0)

        def NULL(self):
            return self.getToken(MyLangParser.NULL, 0)

        def BOOL(self):
            return self.getToken(MyLangParser.BOOL, 0)

        def call(self):
            return self.getTypedRuleContext(MyLangParser.CallContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MyLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(MyLangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(MyLangParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(MyLangParser.INT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.match(MyLangParser.FLOAT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.match(MyLangParser.NULL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 42
                self.match(MyLangParser.BOOL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 43
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






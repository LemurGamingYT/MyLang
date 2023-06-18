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
        4,1,18,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,1,1,1,1,2,1,2,3,2,40,8,2,
        1,2,1,2,3,2,44,8,2,3,2,46,8,2,1,3,1,3,3,3,50,8,3,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,3,5,60,8,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,68,8,6,1,
        6,1,6,1,7,1,7,1,7,5,7,75,8,7,10,7,12,7,78,9,7,1,8,1,8,1,8,5,8,83,
        8,8,10,8,12,8,86,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,96,8,9,
        1,9,1,9,1,9,5,9,101,8,9,10,9,12,9,104,9,9,1,9,0,1,18,10,0,2,4,6,
        8,10,12,14,16,18,0,0,112,0,23,1,0,0,0,2,28,1,0,0,0,4,45,1,0,0,0,
        6,49,1,0,0,0,8,51,1,0,0,0,10,55,1,0,0,0,12,64,1,0,0,0,14,71,1,0,
        0,0,16,79,1,0,0,0,18,95,1,0,0,0,20,22,3,4,2,0,21,20,1,0,0,0,22,25,
        1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,
        26,27,5,0,0,1,27,1,1,0,0,0,28,32,5,3,0,0,29,31,3,4,2,0,30,29,1,0,
        0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,
        1,0,0,0,35,36,5,4,0,0,36,3,1,0,0,0,37,39,3,18,9,0,38,40,5,6,0,0,
        39,38,1,0,0,0,39,40,1,0,0,0,40,46,1,0,0,0,41,43,3,6,3,0,42,44,5,
        6,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,37,1,0,0,0,45,
        41,1,0,0,0,46,5,1,0,0,0,47,50,3,8,4,0,48,50,3,10,5,0,49,47,1,0,0,
        0,49,48,1,0,0,0,50,7,1,0,0,0,51,52,5,11,0,0,52,53,5,5,0,0,53,54,
        3,18,9,0,54,9,1,0,0,0,55,56,5,9,0,0,56,57,5,11,0,0,57,59,5,1,0,0,
        58,60,3,16,8,0,59,58,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,
        2,0,0,62,63,3,2,1,0,63,11,1,0,0,0,64,65,5,11,0,0,65,67,5,1,0,0,66,
        68,3,14,7,0,67,66,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,70,5,2,
        0,0,70,13,1,0,0,0,71,76,3,18,9,0,72,73,5,8,0,0,73,75,3,18,9,0,74,
        72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,15,1,0,0,
        0,78,76,1,0,0,0,79,84,5,11,0,0,80,81,5,8,0,0,81,83,5,11,0,0,82,80,
        1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,17,1,0,0,0,
        86,84,1,0,0,0,87,88,6,9,-1,0,88,96,5,11,0,0,89,96,5,12,0,0,90,96,
        5,13,0,0,91,96,5,14,0,0,92,96,5,15,0,0,93,96,5,16,0,0,94,96,3,12,
        6,0,95,87,1,0,0,0,95,89,1,0,0,0,95,90,1,0,0,0,95,91,1,0,0,0,95,92,
        1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,102,1,0,0,0,97,98,10,2,0,
        0,98,99,5,10,0,0,99,101,3,18,9,3,100,97,1,0,0,0,101,104,1,0,0,0,
        102,100,1,0,0,0,102,103,1,0,0,0,103,19,1,0,0,0,104,102,1,0,0,0,12,
        23,32,39,43,45,49,59,67,76,84,95,102
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'='", "';'", 
                     "'.'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "EQUALS", "SEMI", "DOT", "COMMA", "FUNC", "ARITHOPS", 
                      "ID", "STRING", "INT", "FLOAT", "NULL", "BOOL", "WHITESPACE", 
                      "COMMENT" ]

    RULE_parse = 0
    RULE_block = 1
    RULE_stmt = 2
    RULE_assignments = 3
    RULE_var_assignment = 4
    RULE_func_assignment = 5
    RULE_call = 6
    RULE_args = 7
    RULE_params = 8
    RULE_expr = 9

    ruleNames =  [ "parse", "block", "stmt", "assignments", "var_assignment", 
                   "func_assignment", "call", "args", "params", "expr" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    LBRACE=3
    RBRACE=4
    EQUALS=5
    SEMI=6
    DOT=7
    COMMA=8
    FUNC=9
    ARITHOPS=10
    ID=11
    STRING=12
    INT=13
    FLOAT=14
    NULL=15
    BOOL=16
    WHITESPACE=17
    COMMENT=18

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
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 129536) != 0:
                self.state = 20
                self.stmt()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(MyLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MyLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MyLangParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StmtContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MyLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(MyLangParser.LBRACE)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 129536) != 0:
                self.state = 29
                self.stmt()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(MyLangParser.RBRACE)
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

        def assignments(self):
            return self.getTypedRuleContext(MyLangParser.AssignmentsContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MyLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.expr(0)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 38
                    self.match(MyLangParser.SEMI)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.assignments()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 42
                    self.match(MyLangParser.SEMI)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_assignment(self):
            return self.getTypedRuleContext(MyLangParser.Var_assignmentContext,0)


        def func_assignment(self):
            return self.getTypedRuleContext(MyLangParser.Func_assignmentContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_assignments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignments" ):
                return visitor.visitAssignments(self)
            else:
                return visitor.visitChildren(self)




    def assignments(self):

        localctx = MyLangParser.AssignmentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignments)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.var_assignment()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.func_assignment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def EQUALS(self):
            return self.getToken(MyLangParser.EQUALS, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_var_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assignment" ):
                return visitor.visitVar_assignment(self)
            else:
                return visitor.visitChildren(self)




    def var_assignment(self):

        localctx = MyLangParser.Var_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MyLangParser.ID)
            self.state = 52
            self.match(MyLangParser.EQUALS)
            self.state = 53
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MyLangParser.FUNC, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def params(self):
            return self.getTypedRuleContext(MyLangParser.ParamsContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_func_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_assignment" ):
                return visitor.visitFunc_assignment(self)
            else:
                return visitor.visitChildren(self)




    def func_assignment(self):

        localctx = MyLangParser.Func_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(MyLangParser.FUNC)
            self.state = 56
            self.match(MyLangParser.ID)
            self.state = 57
            self.match(MyLangParser.LPAREN)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 58
                self.params()


            self.state = 61
            self.match(MyLangParser.RPAREN)
            self.state = 62
            self.block()
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
        self.enterRule(localctx, 12, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MyLangParser.ID)
            self.state = 65
            self.match(MyLangParser.LPAREN)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0:
                self.state = 66
                self.args()


            self.state = 69
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
        self.enterRule(localctx, 14, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.expr(0)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 72
                self.match(MyLangParser.COMMA)
                self.state = 73
                self.expr(0)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.ID)
            else:
                return self.getToken(MyLangParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.COMMA)
            else:
                return self.getToken(MyLangParser.COMMA, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = MyLangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MyLangParser.ID)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 80
                self.match(MyLangParser.COMMA)
                self.state = 81
                self.match(MyLangParser.ID)
                self.state = 86
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
            self.op = None # Token

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


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def ARITHOPS(self):
            return self.getToken(MyLangParser.ARITHOPS, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 88
                self.match(MyLangParser.ID)
                pass

            elif la_ == 2:
                self.state = 89
                self.match(MyLangParser.STRING)
                pass

            elif la_ == 3:
                self.state = 90
                self.match(MyLangParser.INT)
                pass

            elif la_ == 4:
                self.state = 91
                self.match(MyLangParser.FLOAT)
                pass

            elif la_ == 5:
                self.state = 92
                self.match(MyLangParser.NULL)
                pass

            elif la_ == 6:
                self.state = 93
                self.match(MyLangParser.BOOL)
                pass

            elif la_ == 7:
                self.state = 94
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyLangParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 97
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 98
                    localctx.op = self.match(MyLangParser.ARITHOPS)
                    self.state = 99
                    self.expr(3) 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         





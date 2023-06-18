# Generated from core/MyLang.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete generic visitor for a parse tree produced by MyLangParser.

class MyLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLangParser#parse.
    def visitParse(self, ctx:MyLangParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#block.
    def visitBlock(self, ctx:MyLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#stmt.
    def visitStmt(self, ctx:MyLangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#assignments.
    def visitAssignments(self, ctx:MyLangParser.AssignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#var_assignment.
    def visitVar_assignment(self, ctx:MyLangParser.Var_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#func_assignment.
    def visitFunc_assignment(self, ctx:MyLangParser.Func_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#call.
    def visitCall(self, ctx:MyLangParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#args.
    def visitArgs(self, ctx:MyLangParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#params.
    def visitParams(self, ctx:MyLangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#expr.
    def visitExpr(self, ctx:MyLangParser.ExprContext):
        return self.visitChildren(ctx)



del MyLangParser
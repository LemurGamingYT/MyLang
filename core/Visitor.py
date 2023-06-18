from .gen.MyLangVisitor import MyLangVisitor
from .gen.MyLangParser import MyLangParser

from .env import Environment
from .reprs import *

from os import listdir

class Visitor(MyLangVisitor):
    def __init__(self) -> None:
        self.env = Environment()
    
    def visitArgs(self, ctx: MyLangParser.ArgsContext):
        args = []
        for expr in ctx.expr():
            expr = self.visitExpr(expr)
            
            if isinstance(expr, idRepr):
                expr = self.env.get_var_value(expr.value)
            
            args.append(expr)
        
        return args
    
    def visitParams(self, ctx: MyLangParser.ParamsContext):
        return [param for param in ctx.ID()]
        
    def visitCall(self, ctx: MyLangParser.CallContext):
        funcs_list = set(listdir("core/funcs/"))
        func_name = str(ctx.ID())
        
        args = self.visitArgs(ctx.args()) if ctx.args() is not None else []
        
        if "_" + func_name + ".py" in funcs_list:
            exec("import core.funcs._{name} as _{name}; _{name}._{name}({args})".format(name = func_name, args = args))
        elif self.env.functions.get(func_name) is not None:
            self.visitBlock(self.env.get_func(func_name).block)
    
    def visitExpr(self, ctx: MyLangParser.ExprContext):
        if ctx.call() is not None:
            return self.visitCall(ctx.call())
        elif ctx.op is not None:
            op = ctx.op.text
            
            val1 = self.visitExpr(ctx.expr(0))
            val2 = self.visitExpr(ctx.expr(1))
            
            return eval("{}{}{}".format(val1, op, val2))
        else:
            for atom in ("ID", "STRING", "INT", "FLOAT", "NULL", "BOOL"):
                value = str(getattr(ctx, atom)())
                if value != "None":
                    form = atom.lower() + "Repr"
                    r = globals().get(form)
                    if r is not None:
                        if form == "stringRepr":
                            value = value[1:-1]
                        elif form == "intRepr":
                            value = int(value)
                        elif form == "floatRepr":
                            value = float(value)
                        elif form == "boolRepr":
                            value = bool(value.title())
                        
                        return r(value)
    
    def visitFunc_assignment(self, ctx: MyLangParser.Func_assignmentContext):
        name = str(ctx.ID())
        params = self.visitParams(ctx.params()) if ctx.params() is not None else []
        block = ctx.block()
        
        self.env.add_func(funcRepr(name, params, block))
    
    def visitVar_assignment(self, ctx: MyLangParser.Var_assignmentContext):
        name = str(ctx.ID())
        constant = name.isupper()
        
        value = self.visitExpr(ctx.expr())
        
        self.env.add_var(varRepr(name, value, constant))

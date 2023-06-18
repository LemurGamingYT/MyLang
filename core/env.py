from .reprs import varRepr, funcRepr
from typing import Dict

class Environment:
    def __init__(self):
        self.variables: Dict[str: varRepr] = {}
        self.functions: Dict[str: funcRepr] = {}
    
    def add_var(self, representation: varRepr):
        self.variables[representation.name] = representation
    
    def get_var(self, name: str):
        return self.variables[name]
    
    def get_var_value(self, name: str):
        return self.variables[name].value
    
    def remove_var(self, name: str):
        self.variables.pop(name)
    
    def add_func(self, representation: funcRepr):
        self.functions[representation.name] = representation
    
    def get_func(self, name: str):
        return self.functions[name]
    
    def remove_func(self, name: str):
        self.functions.pop(name)

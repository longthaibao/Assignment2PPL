from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):
    # program: nllist decllist EOF;
    def visitProgram(self,ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.nllist()),self.visit(ctx.decllist()))
    
    # decllist: decl decllist | decl;
    def visitDecllist(self,ctx:ZCodeParser.DecllistContext):
       return self.visit(ctx.decl()) if ctx.getChildCount() == 1 else self.visit(ctx.decl()) + self.visit(ctx.decllist())
        
    # decl: vardecl | funcdecl;
    def visitDecl(self,ctx:ZCodeParser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else:
            return self.visit(ctx.funcdecl())
    # vardecl: (vardecl1 | vardecl2 | vardecl3 | vardecl4) nlprime;
    def visitVardecl(self,ctx:ZCodeParser.VardeclContext):
        return self.visit(ctx.vardecl1()) if ctx.vardecl1() else self.visit(ctx.vardecl2()) if ctx.vardecl2() else self.visit(ctx.vardecl3()) if ctx.vardecl3() else self.visit(ctx.vardecl4())
    # vardecl1: primitype IDENTIFIER (ASSIGN initval)?;
    def visitVardecl1(self,ctx:ZCodeParser.Vardecl1Context):
        primitype = self.visit(ctx.primitype())
        IDENTIFIER = ctx.IDENTIFIER().getText()
        initval = self.visit(ctx.initval()) if ctx.initval() else None
        return list(map(lambda x: VarDecl(x,primitype,IDENTIFIER,initval),self.visit(ctx.nlprime())))


        

    

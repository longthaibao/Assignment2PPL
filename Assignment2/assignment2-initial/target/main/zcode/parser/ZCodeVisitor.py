# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decllist.
    def visitDecllist(self, ctx:ZCodeParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitype.
    def visitPrimitype(self, ctx:ZCodeParser.PrimitypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implitype.
    def visitImplitype(self, ctx:ZCodeParser.ImplitypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraytype.
    def visitArraytype(self, ctx:ZCodeParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sizelist.
    def visitSizelist(self, ctx:ZCodeParser.SizelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array.
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#listofArray.
    def visitListofArray(self, ctx:ZCodeParser.ListofArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayvalue.
    def visitArrayvalue(self, ctx:ZCodeParser.ArrayvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl1.
    def visitVardecl1(self, ctx:ZCodeParser.Vardecl1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl2.
    def visitVardecl2(self, ctx:ZCodeParser.Vardecl2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl3.
    def visitVardecl3(self, ctx:ZCodeParser.Vardecl3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl4.
    def visitVardecl4(self, ctx:ZCodeParser.Vardecl4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#initval.
    def visitInitval(self, ctx:ZCodeParser.InitvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramdecl.
    def visitParamdecl(self, ctx:ZCodeParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramlist.
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramprime.
    def visitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#bodyfunc.
    def visitBodyfunc(self, ctx:ZCodeParser.BodyfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtlist.
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtprime.
    def visitStmtprime(self, ctx:ZCodeParser.StmtprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forstmt.
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignstmt.
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifstmt.
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elstmt.
    def visitElstmt(self, ctx:ZCodeParser.ElstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifpart.
    def visitElifpart(self, ctx:ZCodeParser.ElifpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakstmt.
    def visitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continuestmt.
    def visitContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnstmt.
    def visitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funstmt.
    def visitFunstmt(self, ctx:ZCodeParser.FunstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockstmt.
    def visitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprlist.
    def visitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprprime.
    def visitExprprime(self, ctx:ZCodeParser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr0.
    def visitExpr0(self, ctx:ZCodeParser.Expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr9.
    def visitExpr9(self, ctx:ZCodeParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr10.
    def visitExpr10(self, ctx:ZCodeParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nllist.
    def visitNllist(self, ctx:ZCodeParser.NllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nlprime.
    def visitNlprime(self, ctx:ZCodeParser.NlprimeContext):
        return self.visitChildren(ctx)



del ZCodeParser
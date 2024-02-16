from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):

    def visitProgram(self,ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    
    # decllist: decl decllist | decl;
    def visitDecllist(self, ctx: ZCodeParser.DecllistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        else:
            return [self.visit(ctx.decl)] + self.visit(ctx.decllist())
        
    # decl: vardecl | funcdecl;
    def visitDecl(self,ctx:ZCodeParser.DeclContext):
        return self.visit(ctx.vardecl()) if ctx.vardecl() else self.visit(ctx.funcdecl())
    # vardecl: (vardecl1 | vardecl2 | vardecl3 | vardecl4) nlprime;
    def visitVardecl(self,ctx:ZCodeParser.VardeclContext):
        return self.visit(ctx.vardecl1()) if ctx.vardecl1() else self.visit(ctx.vardecl2()) if ctx.vardecl2() else self.visit(ctx.vardecl3()) if ctx.vardecl3() else self.visit(ctx.vardecl4())
    # vardecl1: primitype IDENTIFIER (ASSIGN initval)?;
    def visitVardecl1(self,ctx:ZCodeParser.Vardecl1Context):
        primitype = self.visit(ctx.primitype())
        IDENTIFIER = ctx.IDENTIFIER().getText()
        initval = self.visit(ctx.initval()) if ctx.initval() else None
        return VarDecl(Id(IDENTIFIER),primitype,None,initval)
    # vardecl2: VAR IDENTIFIER ASSIGN initval;
    def visitVardecl2(self,ctx:ZCodeParser.Vardecl2Context):
        VAR=ctx.VAR().getText()
        IDENTIFIER = ctx.IDENTIFIER().getText()
        initval = self.visit(ctx.initval())
        return VarDecl(Id(IDENTIFIER),None,VAR,initval)
    # vardecl3: DYNAMIC IDENTIFIER (ASSIGN initval)?;
    def visitVardecl3(self,ctx:ZCodeParser.Vardecl3Context):
        DYNAMIC=ctx.DYNAMIC().getText()
        IDENTIFIER = ctx.IDENTIFIER().getText()
        initval = self.visit(ctx.initval()) if ctx.initval() else None
        return VarDecl(Id(IDENTIFIER),None,DYNAMIC,initval)
    # vardecl4: arraytype (ASSIGN expr0)?;
    def visitVardecl4(self,ctx:ZCodeParser.Vardecl4Context):
            arraytype,IDENTIFIER = self.visit(ctx.arraytype())
            expr0 = self.visit(ctx.expr0()) if ctx.expr0() else None
            return VarDecl(Id(IDENTIFIER), arraytype, None, expr0)
    # primitype: BOOL | NUMBER | STRING;
    def visitPrimitype(self,ctx:ZCodeParser.PrimitypeContext):
        return ctx.BOOL() if ctx.BOOL() else ctx.NUMBER() if ctx.NUMBER() else ctx.STRING()
    # implitype: VAR | DYNAMIC;
    def visitImplitype(self,ctx:ZCodeParser.ImplitypeContext):
        return ctx.VAR() if ctx.VAR() else ctx.DYNAMIC()
    # arraytype: primitype IDENTIFIER LEFTBRACKET sizelist RIGHTBRACKET;
    def visitArraytype(self,ctx:ZCodeParser.ArraytypeContext):
        primitype = self.visit(ctx.primitype())
        sizelist = self.visit(ctx.sizelist())
        return ArrayType(sizelist,primitype),ctx.IDENTIFIER().getText()
    # initval: exprlist;
    def visitInitval(self,ctx:ZCodeParser.InitvalContext):
        return self.visit(ctx.exprlist()) 
    # funcdecl: FUNC IDENTIFIER paramdecl ((nllist bodyfunc) | nlprime);
    def visitFuncdecl(self,ctx:ZCodeParser.FuncdeclContext):
        IDENTIFIER = ctx.IDENTIFIER().getText()
        paramdecl = self.visit(ctx.paramdecl())
        if ctx.nllist():
            bodyfunc = self.visit(ctx.bodyfunc())
            return FuncDecl(Id(IDENTIFIER),paramdecl,bodyfunc)
        else:
            return FuncDecl(Id(IDENTIFIER),paramdecl,None)
    # paramdecl: LEFTPAREN paramlist RIGHTPAREN;
    def visitParamdecl(self,ctx:ZCodeParser.ParamdeclContext):
        return self.visit(ctx.paramlist())
    # paramlist: paramprime |;
    def visitParamlist(self,ctx:ZCodeParser.ParamlistContext):
        return self.visit(ctx.paramprime()) if ctx.paramprime() else []
    # paramprime: param COMMA paramprime | param;
    def visitParamprime(self,ctx:ZCodeParser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        else:
            return [self.visit(ctx.param())] + self.visit(ctx.paramprime())
    # param: primitype (IDENTIFIER| IDENTIFIER LEFTBRACKET exprprime RIGHTBRACKET);
    def visitParam(self,ctx:ZCodeParser.ParamContext):
        primitype = self.visit(ctx.primitype())
        if ctx.exprprime():
            IDENTIFIER = ctx.IDENTIFIER().getText()
            exprprime = self.visit(ctx.exprprime())
            return VarDecl(Id(IDENTIFIER),primitype,None,exprprime)
        else:
            return VarDecl(Id(ctx.IDENTIFIER().getText()),primitype,None,None)
    # bodyfunc: returnstmt | blockstmt;
    def visitBodyfunc(self,ctx:ZCodeParser.BodyfuncContext):
        return self.visit(ctx.returnstmt()) if ctx.returnstmt() else self.visit(ctx.blockstmt())
    # stmtlist: stmtprime |;
    def visitStmtlist(self,ctx:ZCodeParser.StmtlistContext):
        return self.visit(ctx.stmtprime()) if ctx.stmtprime() else []
    # stmtprime: (stmt | vardecl nlprime) stmtprime | (stmt | vardecl nlprime);
    def visitStmtprime(self,ctx:ZCodeParser.StmtprimeContext):
        stmts = []
        for child in ctx.getChildren():
            if child.getRuleIndex() == ZCodeParser.RULE_stmt:
                stmts.append(self.visit(child))
            elif child.getRuleIndex() == ZCodeParser.RULE_vardecl:
                stmts.append(self.visit(child))
            elif child.getRuleIndex() == ZCodeParser.RULE_stmtprime:
                stmts += self.visit(child)
        return stmts
    # stmt: (assignstmt | forstmt | ifstmt | breakstmt | continuestmt | returnstmt | funstmt | blockstmt | vardecl);
    def visitStmt(self,ctx:ZCodeParser.StmtContext):
        if ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.forstmt(): 
            return self.visit(ctx.forstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        elif ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        elif ctx.funstmt():
            return self.visit(ctx.funstmt())
        elif ctx.blockstmt():
            return self.visit(ctx.blockstmt())
        elif ctx.vardecl():
            return self.visit(ctx.vardecl())
        # assignstmt: (IDENTIFIER| (IDENTIFIER LEFTBRACKET exprprime RIGHTBRACKET)) ASSIGN exprprime nlprime;
    def visitAssignstmt(self,ctx:ZCodeParser.AssignstmtContext):
        IDENTIFIER = ctx.IDENTIFIER().getText()
        exprprime= self.visit(ctx.exprprime(1))
        return Assign(IDENTIFIER,exprprime)
    # forstmt: FOR IDENTIFIER (ASSIGN exprlist)? UNTIL exprprime BY exprprime nllist stmtprime;
    def visitForstmt(self,ctx:ZCodeParser.ForstmtContext):
        IDENTIFIER = ctx.IDENTIFIER().getText()
        exprprime1 = self.visit(ctx.exprprime(0))
        exprprime2 = self.visit(ctx.exprprime(1))
        stmtprime = self.visit(ctx.stmtprime())
        return For(IDENTIFIER,exprprime1,exprprime2,stmtprime)
    # assignstmt: (IDENTIFIER | (IDENTIFIER LEFTBRACKET exprprime RIGHTBRACKET)) ASSIGN exprprime nlprime;
    def visitAssignstmt(self,ctx:ZCodeParser.AssignstmtContext):
        IDENTIFIER = ctx.IDENTIFIER().getText()
        exprprime = self.visit(ctx.exprprime())
        return Assign(IDENTIFIER,exprprime)
    # ifstmt: (IF LEFTPAREN expr0 RIGHTPAREN nllist stmt) elstmt (ELSE nllist stmt)?;
    def visitIfstmt(self,ctx:ZCodeParser.IfstmtContext):
        expr0 = self.visit(ctx.expr0())
        stmt = self.visit(ctx.stmt(0))
        elstmt = self.visit(ctx.elstmt())
        if ctx.ELSE():
            stmt1 = self.visit(ctx.stmt(1))
            return If(expr0,stmt,elstmt,stmt1)
        else:
            return If(expr0,stmt,elstmt)
    # breakstmt: BREAK nlprime;
    def visitBreakstmt(self,ctx:ZCodeParser.BreakstmtContext):
        return Break()
    # continuestmt: CONTINUE nlprime;
    def visitContinuestmt(self,ctx:ZCodeParser.ContinuestmtContext):
        return Continue()
    # returnstmt: RETURN exprlist nlprime;
    def visitReturnstmt(self,ctx:ZCodeParser.ReturnstmtContext):
        exprlist = self.visit(ctx.exprlist())
        return Return(exprlist)
    # funstmt: IDENTIFIER LEFTPAREN exprlist RIGHTPAREN nlprime;
    def visitFunstmt(self,ctx:ZCodeParser.FunstmtContext):
        IDENTIFIER = ctx.IDENTIFIER().getText()
        exprlist = self.visit(ctx.exprlist())
        return CallStmt(IDENTIFIER,exprlist)
    # blockstmt: BEGIN nlprime stmtlist END nlprime;
    def visitBlockstmt(self,ctx:ZCodeParser.BlockstmtContext):
        stmtlist = self.visit(ctx.stmtlist())
        return Block(stmtlist)
    # elstmt: elprime |;
    def visitElstmt(self,ctx:ZCodeParser.ElstmtContext):
        return self.visit(ctx.elprime()) if ctx.elprime() else []
    # elprime: ELIF LEFTPAREN expr0 RIGHTPAREN nllist stmt elprime| ELIF LEFTPAREN expr0 RIGHTPAREN nllist stmt;
    def visitElprime(self,ctx:ZCodeParser.ElprimeContext):
        expr0 = self.visit(ctx.expr0())
        stmt = self.visit(ctx.stmt())
        if ctx.elprime():
            return [(expr0,stmt)] + self.visit(ctx.elprime())
        else:
            return [(expr0,stmt)]
    # exprlist: exprprime |;
    def visitExprlist(self,ctx:ZCodeParser.ExprlistContext):
        return self.visit(ctx.exprprime()) if ctx.exprprime() else []
    # exprprime: expr0 COMMA exprprime | expr0;
    def visitExprprime(self,ctx:ZCodeParser.ExprprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr0())]
        else:
            return [self.visit(ctx.expr0())] + self.visit(ctx.exprprime())
    # expr0: expr1 CONCATENATION expr1 | expr1;
    def visitExpr0(self, ctx: ZCodeParser.Expr0Context):
        if ctx.CONCATENATION():
            return BinaryOp(ctx.CONCATENATION().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        else:
            return self.visit(ctx.expr1(0))
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
    # expr3: expr3 (PLUS | MINUS) expr4 | expr4;
    def visitExpr3(self, ctx: ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
    # expr4: expr4 ( TIMES | DIVIDED | MOD) expr5 | expr5;
    def visitExpr4(self, ctx: ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: ZCodeParser.Expr5Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr6())
    # expr6: MINUS expr6 | expr7;
    def visitExpr6(self, ctx: ZCodeParser.Expr6Context):
        if ctx.MINUS():
            return UnaryOp(ctx.MINUS().getText(), self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.expr7())
    # expr7: IDENTIFIER (LEFTPAREN exprlist RIGHTPAREN)? LEFTBRACKET exprprime RIGHTBRACKET| expr8;
    def visitExpr7(self, ctx: ZCodeParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        else:
            IDENTIFIER = ctx.IDENTIFIER().getText()
            exprlist = self.visit(ctx.exprlist()) if ctx.exprlist() else []
            exprprime = self.visit(ctx.exprprime())
            return CallExpr(Id(IDENTIFIER),exprlist) if ctx.LEFTPAREN() else ArrayCell(Id(IDENTIFIER),exprprime)
    # expr8: IDENTIFIER LEFTPAREN exprlist RIGHTPAREN | expr9;
    def visitExpr8(self, ctx: ZCodeParser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr9())
        else:
            IDENTIFIER = ctx.IDENTIFIER().getText()
            exprlist = self.visit(ctx.exprlist())
            return CallExpr(Id(IDENTIFIER),exprlist)
    # expr9: NUMBER_LITERAL | STRING_LITERAL | BOOLEAN_LITERAL | IDENTIFIER | array | expr10;
    def visitExpr9(self, ctx: ZCodeParser.Expr9Context):
        if ctx.NUMBER_LITERAL():
            return NumberLiteral(int(ctx.NUMBER_LITERAL().getText()))
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(ctx.BOOLEAN_LITERAL().getText())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.array():
            return self.visit(ctx.array())
        else:
            return self.visit(ctx.expr10())
    # expr10: LEFTPAREN expr0 RIGHTPAREN;
    def visitExpr10(self, ctx: ZCodeParser.Expr10Context):
        return self.visit(ctx.expr0())
    # nllist: nlprime |;
    def visitNllist(self, ctx: ZCodeParser.NllistContext):
        return self.visit(ctx.nlprime()) if ctx.nlprime() else []
    # nlprime: NL nlprime | NL;
    def visitNlprime(self, ctx: ZCodeParser.NlprimeContext):
        return self.visit(ctx.nlprime()) if ctx.nlprime() else []

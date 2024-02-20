/* 2113443 */
grammar ZCode;

@lexer::header {
# 2113443
from lexererr import *
}

options {
	language=Python3;
}


program: nllist decllist EOF;

decllist: decl decllist | decl;
decl: vardecl | funcdecl;


// VARIABLE DECLARATION
vardecl: (var1decl|var2decl|var3decl|var4decl) nlprime;

nllist: nlprime | ; // nullable list of newline
nlprime: NEWLINE nlprime | NEWLINE; // non-nullable list of newline

var1decl: typevar IDEN ASSIGN exp | typevar IDEN;
var2decl: VAR IDEN ASSIGN exp;
var3decl: DYNAMIC IDEN ASSIGN exp | DYNAMIC IDEN;
var4decl: typevar IDEN LBRAC dime RBRAC arrinit | typevar IDEN LBRAC dime RBRAC;

arrinit: ASSIGN LBRAC expprime RBRAC;
dime: LIT_NUMBER COMMA dime | LIT_NUMBER; //1,2

typevar: NUMBER | BOOL | STRING;

//FUNCTION DECLARATION

funcdecl: func1decl | func2decl;
func1decl: FUNC IDEN paramdecl nllist body;
func2decl: FUNC IDEN paramdecl nlprime;
// vardecl_nonl: var1decl;
paramdecl: LPAR paramlist RPAR;
paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;
// param: vardecl_nonl;
param: typevar IDEN (LBRAC dime RBRAC|);
body: blockstmt|restmt;

// statement
stmtlist: stmt stmtlist | ;

stmt: vardecl | assignstmt  | ifstmt | forstmt 
    | breakstmt | constmt | restmt | callstmt
    | blockstmt;

blockstmt: BEGIN nlprime stmtlist END nlprime;

assignstmt: (normassign | arrassign) nlprime;
normassign: IDEN ASSIGN exp;
arrassign: (IDEN) LBRAC expprime RBRAC ASSIGN exp; /* remove funcall */ 

ifstmt: IF condition nllist stmt elif_list else_func;
elif_list:	elif_func elif_list | ; // elif a>1 a=b elif b>2 a=c
elif_func:	ELIF condition nllist stmt ; // elif a=b
else_func:	ELSE nllist stmt | ; // else a=b

condition: LPAR exp RPAR;

forstmt: FOR IDEN UNTIL exp BY exp nllist stmt;

breakstmt: BREAK nlprime;
constmt: CONTINUE nlprime;

restmt: RETURN (exp|) nlprime;


callstmt: IDEN LPAR explist RPAR nlprime;



explist: expprime |;
expprime: exp COMMA expprime | exp;

exp: exp1 DOT3 exp1 | exp1;
exp1: exp2 (EQ_STR|EQ_NUM|DIFF|LT|GT|LTE|GTE) exp2 | exp2;
exp2: exp2 (AND|OR) exp3 | exp3;
exp3: exp3 (ADD|SUB) exp4 | exp4;
exp4: exp4 (MUL|DIV|MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7: (IDEN|funcall) indexop | exp8;
exp8: LIT_BOOLEAN | LIT_NUMBER | LIT_STRING | IDEN | arraylit | funcall | exp9;
exp9: LPAR exp RPAR;

arraylit: LBRAC expprime RBRAC;
indexop: LBRAC expprime RBRAC;
funcall: IDEN LPAR explist RPAR;


// *****************COMMENT*******************
// ## This is a single comment.
// COMMENT:  ('^##'|([\n\r] [\n\t\r ]* '##')) ~[\r\n]* -> skip;
// COMMENT: '^' '##' .*? ('\n'|EOF) ->skip;

COMMENT: '##' ~[\r\n]* -> skip;
// *****************LITERALS*******************

LIT_NUMBER  : DIGIT+ ('.' DIGIT*)? (('e'|'E')('+'|'-')?DIGIT+)?;
fragment DIGIT: [0-9];


LIT_BOOLEAN : TRUE | FALSE;

LIT_STRING  : '"' LIT_CHAR* '"'
            {self.text = self.text[1:-1]};

fragment LIT_CHAR: ESC|'\'"'  | ~[\\\r\n"];
fragment ESC: [\\] [btnfr'\\];
// *****************KEYWORDS*******************

TRUE    : 'true';
FALSE   : 'false';
NUMBER  : 'number';
BOOL    : 'bool';
STRING  : 'string';
RETURN  : 'return';
VAR     : 'var';
DYNAMIC : 'dynamic';
FUNC    : 'func';
FOR     : 'for';
UNTIL   : 'until';
BY      : 'by';
BREAK   : 'break';
CONTINUE: 'continue';
IF      : 'if';
ELSE    : 'else';
ELIF    : 'elif';
BEGIN   : 'begin';
END     : 'end';
NOT     : 'not';
AND     : 'and';
OR      : 'or';

// *****************OPERATORS*******************

ADD     : '+';
SUB     : '-';
MUL     : '*';
DIV     : '/';
MOD     : '%';
// NOT AND OR already declared in KEYWORDS
EQ_NUM  : '=';
ASSIGN  : '<-';
DIFF    : '!=';
LT      : '<';
LTE     : '<=';
GT      : '>';
GTE     : '>=';
DOT3    : '...';
EQ_STR  : '==';

// *****************SEPARATORS*******************

LPAR    : '(';
RPAR    : ')';
LBRAC   : '[';
RBRAC   : ']';
COMMA   : ',';
NEWLINE : '\n';





IDEN    : [A-Za-z_][A-Za-z_0-9]*;
WS      : [ \b\f\t\r]+ -> skip ; // skip spaces, tabs, newlines
UNCLOSE_STRING: '"' LIT_CHAR* ([\n\r]| EOF) {
        ESC = ['\r', '\n']
        text = str(self.text)
        if text[-1] in ESC:
            raise UncloseString(text[1:-1])
        else: #EOF
            raise UncloseString(text[1:]) 
    };
ILLEGAL_ESCAPE:
	'"' LIT_CHAR* ('\\' ~[bfrnt'\\]) {
    y = str(self.text)
    raise IllegalEscape(y[1:])
};
ERROR_CHAR: .{raise ErrorToken(self.text)};
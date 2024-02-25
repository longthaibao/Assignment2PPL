// 2113946
grammar ZCode;

@lexer::header {
# 2113946 - Thai Bao Long
from lexererr import *
}
options {
	language = Python3;
}

program: nllist decllist EOF;

decllist: decl decllist | decl;
decl: vardecl | funcdecl;

//Type and value
primitype: BOOL | NUMBER | STRING;
implitype: VAR | DYNAMIC;
arraytype:
	primitype IDENTIFIER LEFTBRACKET sizelist RIGHTBRACKET;
sizelist: (NUMBER_LITERAL COMMA sizelist) | NUMBER_LITERAL;

array: LEFTBRACKET (exprprime) RIGHTBRACKET;
listofArray: (array COMMA listofArray) | array;
arrayvalue: (LEFTBRACKET (listofArray | exprprime) RIGHTBRACKET);
//VARIABLE DECLARATION
vardecl: (vardecl1 | vardecl2 | vardecl3 | vardecl4) nlprime;
vardecl1: primitype IDENTIFIER (ASSIGN initval)?;
vardecl2: VAR IDENTIFIER ASSIGN initval;
vardecl3: DYNAMIC IDENTIFIER (ASSIGN initval)?;
vardecl4: arraytype (ASSIGN expr0)?;
initval: expr0;

//FUNCTION DECLARATION
funcdecl:
	FUNC IDENTIFIER paramdecl ((nllist bodyfunc) | nlprime);
paramdecl: LEFTPAREN paramlist RIGHTPAREN;
paramlist: paramprime |;
paramprime: param COMMA paramprime | param;
param:
	primitype (
		IDENTIFIER
		| IDENTIFIER LEFTBRACKET sizelist RIGHTBRACKET
	);
bodyfunc: returnstmt | blockstmt;
//Statement
stmtlist: stmtprime |;
stmtprime: (stmt | vardecl nlprime) stmtprime
	| (stmt | vardecl nlprime);
stmt:
	(
		assignstmt
		| forstmt
		| ifstmt
		| breakstmt
		| continuestmt
		| returnstmt
		| funstmt
		| blockstmt
		| vardecl
	);
forstmt: FOR IDENTIFIER UNTIL expr0 BY expr0 nllist stmt;
assignstmt: (
		IDENTIFIER
		| (IDENTIFIER LEFTBRACKET exprprime RIGHTBRACKET)
	) ASSIGN expr0 nlprime;
// ifstmt: (IF LEFTPAREN expr0 RIGHTPAREN nllist stmt) elstmt ( ELSE nllist stmt )?; if if elif if
// else if elif else
ifstmt:
	IF LEFTPAREN expr0 RIGHTPAREN nllist stmt
	| IF LEFTPAREN expr0 RIGHTPAREN nllist stmt elstmt
	| IF LEFTPAREN expr0 RIGHTPAREN nllist stmt ELSE nllist stmt
	| IF LEFTPAREN expr0 RIGHTPAREN nllist stmt elstmt ELSE nllist stmt;
breakstmt: BREAK nlprime;
continuestmt: CONTINUE nlprime;
returnstmt: RETURN (expr0 |) nlprime;
funstmt: IDENTIFIER LEFTPAREN exprlist RIGHTPAREN nlprime;
blockstmt: BEGIN nlprime stmtlist END nlprime;
elstmt: elprime |;
elprime:
	ELIF LEFTPAREN expr0 RIGHTPAREN nllist stmt elprime
	| ELIF LEFTPAREN expr0 RIGHTPAREN nllist stmt;
//Expression
exprlist: exprprime |;
exprprime: expr0 COMMA exprprime | expr0;
expr0: expr1 CONCATENATION expr1 | expr1;
expr1:
	expr2 (EQUAL | COMPARE | NOT_EQUAL | LT | GT | LTOE | GTOE) expr2
	| expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (PLUS | MINUS) expr4 | expr4;
expr4: expr4 ( TIMES | DIVIDED | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7:
	IDENTIFIER (LEFTPAREN exprlist RIGHTPAREN)? LEFTBRACKET exprprime RIGHTBRACKET
	| expr8;
expr8: IDENTIFIER LEFTPAREN exprlist RIGHTPAREN | expr9;
expr9:
	NUMBER_LITERAL
	| STRING_LITERAL
	| BOOLEAN_LITERAL
	| IDENTIFIER
	| array
	| expr10;
expr10: LEFTPAREN expr0 RIGHTPAREN;
nllist: nlprime |;
nlprime: NL nlprime | NL;

// COMMENT
ZCODE_COMMENT: '##' ~[\n]* -> skip;
//KEYWORD

//TYPE LITERAL
BOOLEAN_LITERAL: 'true' | 'false';

RETURN: 'return';
FOR: 'for';
IF: 'if';
NOT: 'not';
VAR: 'var';
UNTIL: 'until';
ELSE: 'else';
AND: 'and';
NUMBER: 'number';
DYNAMIC: 'dynamic';
BY: 'by';
ELIF: 'elif';
OR: 'or';
BOOL: 'bool';
FUNC: 'func';
BREAK: 'break';
BEGIN: 'begin';
STRING: 'string';
CONTINUE: 'continue';
END: 'end';
// Operators

PLUS: '+';
MINUS: '-';
TIMES: '*';
DIVIDED: '/';
MOD: '%';
COMPARE: '==';
EQUAL: '=';
ASSIGN: '<-';
NOT_EQUAL: '!=';
LTOE: '<=';
GTOE: '>=';
LT: '<';
GT: '>';
CONCATENATION: '...';
// Separator
LEFTPAREN: '(';
RIGHTPAREN: ')';
LEFTBRACKET: '[';
RIGHTBRACKET: ']';
COMMA: ',';
NL: '\n' | '\r\n' {self.text = '\n'};

// Literals

NUMBER_LITERAL: INTEGERPART (DECIMALPART? EXPONENTPART?)?;
fragment INTEGERPART: [0-9]+;
fragment DECIMALPART: '.' [0-9]*;
fragment EXPONENTPART: [Ee] [+-]? [0-9]+;

STRING_LITERAL:
	DOUBLEQUOTE CHAR* DOUBLEQUOTE {self.text =self.text[1:-1]};
fragment DOUBLEQUOTE: '"';
fragment INVALID_ESC: ('\\' ~[btnfr'\\]);
fragment CHAR: ESC | '\'"' | ~([\n\r] | '"' | '\\');
fragment ESC: '\\' [btnfr'\\];
fragment SIZE: [0-9]+;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
// fragment LETTER: [a-zA-Z]; fragment DIGIT: [0-9]; fragment UNDERSCORE: '_';
WS: [ \t\b\f]+ -> skip; // skip spaces, tabs, newlines
UNCLOSE_STRING:
	'"' CHAR* ([\n\r] | EOF) {
	if self.text[-1] in ['\n','\r','EOF']:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE:
	'"' CHAR* INVALID_ESC {
	illegal_str_from_beginning = str(self.text)
	raise IllegalEscape(illegal_str_from_beginning[1:])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};
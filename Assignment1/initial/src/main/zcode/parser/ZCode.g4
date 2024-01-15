grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decllist EOF;

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
arrayvalue: (LEFTBRACKET listofArray RIGHTBRACKET) | array;
//VARIABLE DECLARATION
vardecl: vardecl1 | vardecl2 | vardecl3 | vardecl4;
vardecl1: primitype IDENTIFIER (ASSIGN initval)?;
vardecl2: VAR IDENTIFIER ASSIGN initval;
vardecl3: DYNAMIC IDENTIFIER (ASSIGN initval)?;
vardecl4: arraytype (ASSIGN arrayvalue)?;
initval: exprlist;

//FUNCTION DECLARATION
funcdecl: FUNC IDENTIFIER paramdecl bodyfunc?;
paramdecl: LEFTPAREN paramlist RIGHTPAREN;
paramlist: paramprime |;
paramprime: param COMMA paramprime | param;
param:
	primitype (
		IDENTIFIER
		| IDENTIFIER LEFTBRACKET exprprime RIGHTBRACKET
	);
bodyfunc: returnstmt | blockstmt;
//Statement
stmtlist: stmtprime |;
stmtprime: (stmt | vardecl) stmtprime | (stmt | vardecl);
stmt:
	assignstmt
	| forstmt
	| ifstmt
	| breakstmt
	| continuestmt
	| returnstmt
	| funstmt
	| blockstmt;
forstmt:
	FOR IDENTIFIER (exprprime |) (ASSIGN exprprime)? UNTIL exprprime BY exprprime stmtprime;
assignstmt: IDENTIFIER (exprprime)* ASSIGN exprprime;
ifstmt: (IF expr0 stmt) (ELIF expr0 stmt)* (ELSE stmt)?;
breakstmt: BREAK;
continuestmt: CONTINUE;
returnstmt: RETURN exprlist;
funstmt: IDENTIFIER LEFTPAREN exprlist RIGHTPAREN;
blockstmt: BEGIN stmtlist END;
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
expr7: IDENTIFIER LEFTBRACKET exprprime RIGHTBRACKET | expr8;
expr8: IDENTIFIER LEFTPAREN exprlist RIGHTPAREN | expr9;
expr9:
	NUMBER_LITERAL
	| STRING_LITERAL
	| BOOLEAN_LITERAL
	| array
	| IDENTIFIER
	| expr10;
expr10: LEFTPAREN expr0 RIGHTPAREN;
// COMMENT
ZCODE_COMMENT: '##' ~[\r\n]* -> skip;
//KEYWORD

RETURN: 'return';
FOR: 'for';
IF: 'if';
NOT: 'NOT';
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
ARRAY: 'array';
// Operators

PLUS: '+';
MINUS: '-';
TIMES: '*';
DIVIDED: '/';
MOD: '%';
EQUAL: '=';
ASSIGN: '<-';
COMPARE: '==';
NOT_EQUAL: '!=';
LT: '<';
GT: '>';
LTOE: '<=';
GTOE: '>=';
CONCATENATION: '...';
// Separator
LEFTPAREN: '(';
RIGHTPAREN: ')';
LEFTBRACKET: '[';
RIGHTBRACKET: ']';
COMMA: ',';
COLON: ':';
SEMI: ';';

// Literals

NUMBER_LITERAL: INTEGERPART (DECIMALPART? EXPONENTPART?)?;
fragment INTEGERPART: [0-9]+;
fragment DECIMALPART: '.' [0-9]*;
fragment EXPONENTPART: [Ee] [+-]? [0-9]+;

BOOLEAN_LITERAL: 'true' | 'false';

STRING_LITERAL:
	DOUBLEQUOTE CHARLIST* DOUBLEQUOTE {self.text =self.text[1:-1]};
fragment CHARLIST: ESCAPE | '\'"' | ~([\n\r] | '"' | '\\');
fragment DOUBLEQUOTE: '"';
fragment ESCAPE:
	'\\' (' b ' | ' f ' | ' r ' | ' n ' | ' t ' | '\'' | '\\');
SIZE: [0-9]+;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
// fragment LETTER: [a-zA-Z]; fragment DIGIT: [0-9]; fragment UNDERSCORE: '_';
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
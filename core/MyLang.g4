grammar MyLang;

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';

EQUALS : '=';
SEMI : ';';
DOT : '.';
COMMA : ',';

FUNC : 'func' | 'fn';

ARITHOPS : '+' | '-' | '*' | '/' | '%' | '^';

ID : [a-zA-Z_][a-zA-Z0-9_]*;
STRING : '"' (~["\r\n] | '""')* '"';
INT : '-'? [0-9]+;
FLOAT : ('-' [0-9]+)? DOT [0-9]*;
NULL : 'null';
BOOL : ('true' | 'false');

WHITESPACE : [ \t\r\n] -> skip;
COMMENT : '#' ~[\r\n]* -> skip;

parse : stmt* EOF;

block : LBRACE stmt* RBRACE;

stmt
    : expr SEMI?
    | assignments SEMI?
    ;

assignments : var_assignment | func_assignment;

var_assignment : ID EQUALS expr;
func_assignment : FUNC ID LPAREN params? RPAREN block;

call : ID LPAREN args? RPAREN;

args : expr (COMMA expr)*;
params : ID (COMMA ID)*;

expr
    : ID
    | STRING
    | INT
    | FLOAT
    | NULL
    | BOOL
    | expr op=ARITHOPS expr
    | call
    ;

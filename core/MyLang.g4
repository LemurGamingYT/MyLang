grammar MyLang;

LPAREN : '(';
RPAREN : ')';

SEMI : ';';
DOT : '.';
COMMA : ',';

ID : [a-zA-Z_][a-zA-Z0-9_]*;
STRING : '"' (~["\r\n] | '""')* '"';
INT : '-'? [0-9]+;
FLOAT : ('-' [0-9]+)? DOT [0-9]*;
NULL : 'null';
BOOL : ('true' | 'false');

WHITESPACE : [ \t\r\n] -> skip;
COMMENT : '#' ~[\r\n]* -> skip;

parse : stmt* EOF;

stmt
    : expr SEMI?
    ;

call : ID LPAREN args? RPAREN;

args : expr (COMMA expr)*;

expr
    : ID
    | STRING
    | INT
    | FLOAT
    | NULL
    | BOOL
    | call
    ;

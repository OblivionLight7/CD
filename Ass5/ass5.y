%{
#include <stdio.h>
void yyerror(char *);
int yylex();
%}

%token IF ELSE ELSEIF AND OR NTEQ EQ LT LTEQ GT GTEQ ID NUM NOT OP

%%

elcond : ifcondition elsec | ifcondition | ifcondition elifc | ifcondition elifc elifscond ;

elifscond : elsec | elifc elifscond;


ifcondition: IF '(' cond ')' '{' stmt '}'  {printf("Parsing Successful of if Condition\n");} 
;

elifc: ELSEIF '(' cond ')' '{' stmt '}' {printf("\nParsing Successful of elseif\n");} 
;
elsec: ELSE '{' stmt '}' {printf("\nParsing Successful of else\n");}
;


cond	: scond  | scond logop scond ;

stmt :  A | A stmt;

scond	: nid | nid relop nid ;

nid	: ID | NUM ;

A : ID '=' nid OP nid ';'| ID '=' nid  ';'; 

logop	: AND | OR | NOT  ;

relop	: NTEQ | EQ | LT | LTEQ | GT | GTEQ ;

%%

int yywrap()
{
return 1;
}

void yyerror(char *s)
{
	printf("\nInvalid Statement\n");
}

int main()
{
	yyparse();
	return 0;
	
}

